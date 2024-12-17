# CloudFront gRPC feature demo

## Introduction
This project is a sample project that allows you to quickly pull up a demo environment using CDK to test CloudFront gRPC related functions.

## Architecture diagram
<img width="790" alt="image" src="https://github.com/user-attachments/assets/8c69c7e1-2142-4fcb-b442-800742856851" />

## Deployment Instructions
### Prerequisites
* Install CDK: https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html
* You already have an ACM certificate for a custom domain name

### Make/push images
* Configure Environment Variables
```
export AWS_ACCOUNT_ID= your-account-id
export AWS_REGION= your-aws-region
```

* Clone the repository:
```
https://github.com/aws-samples/edge-compute-demo.git
```

* Enter the grpc/examples/python/ path
```
docker build --platform linux/amd64 -t grpc-server .
```
* Enter the nginx/ path
```
docker build --platform linux/amd64 -t nginx-server .
```

* Tag images
```
docker tag grpc-server:latest ${AWS_ACCOUNT_ID}.dkr.ecr.<your-aws-region>.amazonaws.com/grpc-server:latest
docker tag nginx-server:latest ${AWS_ACCOUNT_ID}.dkr.ecr.<your-aws-region>.amazonaws.com/nginx-server:latest
```

* Login to ECR
```
aws ecr get-login-password --region <your-aws-region> | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.<your-aws-region>.amazonaws.com
```

* Create ECR repositories
```
aws ecr create-repository --repository-name grpc-server --region <your-aws-region>
aws ecr create-repository --repository-name nginx-server --region <your-aws-region>
```

* Push images to repositories
```
docker push $AWS_ACCOUNT_ID.dkr.ecr.<your-aws-region>.amazonaws.com/grpc-server:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.<your-aws-region>.amazonaws.com/nginx-server:latest
```

### Deploy the stack
* Enter the project root directory
```
cdk deploy
```
