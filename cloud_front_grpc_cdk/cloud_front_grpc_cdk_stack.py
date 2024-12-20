from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ecs as ecs,
    aws_certificatemanager as acm,
    aws_ecs_patterns as ecs_patterns,
    aws_elasticloadbalancingv2 as elbv2,
    aws_iam as iam,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins
)


class CloudFrontGrpcCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 创建ECS集群
        cluster = ecs.Cluster(self, "grpc-demo",
            cluster_name="grpc"
        )

        # 创建任务执行角色
        execution_role = iam.Role(
            self,
            "TaskExecutionRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonECSTaskExecutionRolePolicy"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2ContainerRegistryReadOnly")
            ]
        )
        
        # 引用证书
        alb_certificate = acm.Certificate.from_certificate_arn(
            self, 
            "ALBCertificate",
            certificate_arn="<your-certificate-arn>"  #替换为您的证书arn
        )

        cloudfront_certificate = acm.Certificate.from_certificate_arn(
            self, 
            "CloudfrontCertificate",
            certificate_arn="<your-certificate-arn>"  #替换为您的证书arn
        )
        
        # 创建第一个gRPC服务
        grpc_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "grpc",
            cluster=cluster,
            memory_limit_mib=1024,
            desired_count=1,
            cpu=512,
            listener_port=443,
            certificate=alb_certificate,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("<your-repository-arn>"), #替换为您的grpc server仓库地址
                container_port=50051,
                execution_role=execution_role
            )
        )

        # 修改gRPC服务的目标组配置
        grpc_service.target_group.configure_health_check(
            port="50051"
        )

        # 设置目标组的协议版本为 GRPC
        cfn_target_group = grpc_service.target_group.node.default_child
        cfn_target_group.protocol_version = "GRPC"

        # 创建Nginx服务的任务定义和服务
        nginx_task_definition = ecs.FargateTaskDefinition(self, "NginxTaskDef",
            memory_limit_mib=1024,
            cpu=512,
            execution_role=execution_role
        )

        nginx_container = nginx_task_definition.add_container("nginx",
            image=ecs.ContainerImage.from_registry("<your-repository-arn>"), #替换为您的nginx server仓库地址
            memory_limit_mib=1024
        )

        nginx_container.add_port_mappings(
            ecs.PortMapping(container_port=80)
        )

        # 创建Nginx服务
        nginx_service = ecs.FargateService(self, "nginx-service",
            cluster=cluster,
            task_definition=nginx_task_definition,
            desired_count=1
        )

        # 为Nginx服务创建目标组
        nginx_target_group = elbv2.ApplicationTargetGroup(self, "nginx-target-group",
            vpc=cluster.vpc,
            port=80,
            protocol=elbv2.ApplicationProtocol.HTTP,
            targets=[nginx_service]
        )

        # 清除默认监听器规则
        grpc_service.listener.node.try_remove_child('DefaultAction')

        # 为Nginx服务添加/http路径的监听器规则
        grpc_service.listener.add_action(
            "http-route",
            action=elbv2.ListenerAction.forward([nginx_target_group]),
            conditions=[
                elbv2.ListenerCondition.path_patterns(["/http/*"])
            ],
            priority=1
        )

        # 添加默认规则，将其他所有请求路由到gRPC服务
        grpc_service.listener.add_action(
            "default-route",
            action=elbv2.ListenerAction.forward([grpc_service.target_group]),
            conditions=[elbv2.ListenerCondition.path_patterns(["/*"])], 
            priority=2
        )
