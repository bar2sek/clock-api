from aws_cdk import core as cdk
import aws_cdk.aws_lambda as lambda_
import path as path
# from aws_cdk.aws_s3 import Bucket
# from aws_cdk.aws_s3_deployment import BucketDeployment, Source

class ClockApiStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # bucket = Bucket(self, "Bucket",
        #     versioned=True,
        #     website_index_document="index.html",
        #     removal_policy=cdk.RemovalPolicy.DESTROY,
        #     auto_delete_objects=True,
        #     bucket_name="client-application-bucket-for-ryan-38058130483"
        # )
        
        # bucket_deployment = BucketDeployment(self, "file",
        #     sources=[Source.asset('front_end')],
        #     destination_bucket=bucket
        # )

        # lambda_.Function(self, "MyLambda",
        #     code=lambda_.Code.from_asset(path.join(__dirname, "my-lambda-handler")),
        #     handler="index.main",
        #     runtime=lambda_.Runtime.PYTHON_3_6
        # )