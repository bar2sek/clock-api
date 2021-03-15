from aws_cdk import core as cdk
from aws_cdk.aws_lambda import lambda
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_s3_deployment import BucketDeployment, Source

class ClockApiStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = Bucket(self, "Bucket",
            versioned=True,
            website_index_document="index.html",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            bucket_name="client-application-bucket-for-ryan-38058130483"
        )
        
        bucket_deployment = BucketDeployment(self, "index",
            sources=[Source.asset('front_end')],
            destination_bucket=bucket
        )