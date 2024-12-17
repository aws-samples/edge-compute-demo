#!/usr/bin/env python3

import aws_cdk as cdk

from cloud_front_grpc_cdk.cloud_front_grpc_cdk_stack import CloudFrontGrpcCdkStack


app = cdk.App()
CloudFrontGrpcCdkStack(app, "CloudFrontGrpcCdkStack")

app.synth()
