import boto3
import time

client = boto3.client(
    "elasticbeanstalk",
    region_name="us-east-1",
    aws_access_key_id="ASIA3REMKRJ4H6OTKH6W",
    aws_secret_access_key="2MA+BG6G3oABRJv1g6DOHJ/9rvJhwFiy/5b+K2Z+",
    aws_session_token="FwoGZXIvYXdzEAwaDCqvlLD0Xj1Gy2ZW1iLIAc8ge8LaTTAszMi5CJhXBIBsSFS7ftAaJu8eoBF1JT4YRV4/zHhj9yN0p1vNGCc280P9YrO95+ybhEopzi4HSM8X2w7awfNhQeXGSqRRDzq3t6heXo+SI2TcMGe5y3vxgaHqZWBy8g0lndcDsmmLfxbLQfkz7xrs69XTfUSlhlIQ5XsW1tmKno93SGNe6PKmiW57BMpcPiQpYYrTh8yUCcI6KRsocKgV9vPjr8NUFC/rG70W9YGMy+ss85UktNAZ1F0ZrcHClsdMKODEhYoGMi0KYsMCU0PHzK0mqeVspkn+0aNYvlpNk2N3nlhqq1wXOXx+V03Ibtz3w+Nm7dY=",
)

# client=boto3.client('cloudfront',region_name='us-east-1',aws_access_key_id='ASIAUUABOLHWSD43LFMZ',
# aws_secret_access_key='Pro8EKnhoEymLnrO22aVIS3usJNCWWI/FpdYcroj',aws_session_token='FwoGZXIvYXdzEAEaDA+b/rTEX92ezZdwZCLHAVDZsl8dVkP6aM9lL9+AHgVGQDK0ByJ+38inxcXYrRi+7nIqMOKi5Z1J+izn75CTftp7016GO+OvraWyRZFUNJyp1CmwlYrJS0eWy4r+i6XAZRKYzTRbPmaBJmpQpf8x0M/CDl/8nN6U2EsUNtVyGpKiezgPOlxg5fvX7AID0feWayrxnmYWE3WjZeP2EEGr/jLDQjeesYi3OCVourwAxhK2u8nK826cbfO30lLUPVFozCj5J6ytq+DWfsdd3eUu71f8HSo92+YoqY2DigYyLRN1znqcoDuz7bDEPrAuy9UmbtSkSHKYM/gNq8oJ+yXEOkopmWg/w+hP1nZv8Q==')


def cloudFront_distribution():
    response = client.create_distribution(
        DistributionConfig={
            "CallerReference": "my-distribution-cdn",
            "DefaultRootObject": "portfolio.html",
            "Origins": {
                "Items": [
                    {
                        "DomainName": "lab3-dynamic-website.s3.us-east-1.amazonaws.com",
                        "S3OriginConfig": {"OriginAccessIdentity": ""},
                        "CustomOriginConfig": {
                            "OriginProtocolPolicy": "http-only"
                            | "match-viewer"
                            | "https-only",
                        },
                    },
                ]
            },
            "OriginGroups": {
                "ViewerProtocolPolicy": "allow-all",
                "AllowedMethods": {
                    "Items": [
                        "GET"
                        | "HEAD"
                        | "POST"
                        | "PUT"
                        | "PATCH"
                        | "OPTIONS"
                        | "DELETE",
                    ],
                    "CachedMethods": {
                        "Items": [
                            "GET"
                            | "HEAD"
                            | "POST"
                            | "PUT"
                            | "PATCH"
                            | "OPTIONS"
                            | "DELETE",
                        ]
                    },
                },
            },
        }
    )
    print(response)


def create_version():
    response = client.create_application_version(
        ApplicationName="my-app-5",
        AutoCreateApplication=True,
        Description="my-app-v4",
        Process=True,
        SourceBundle={
            "S3Bucket": "cloud-1901183-lab4",
            "S3Key": "mysite.zip",
        },
        VersionLabel="v1",
    )
    print(response)


def create_environment():
    response = client.create_environment(
        ApplicationName="my-app-5",
        CNAMEPrefix="my-app-5",
        EnvironmentName="my-env-5",
        SolutionStackName="64bit Amazon Linux 2 v3.3.5 running PHP 8.0",
        VersionLabel="v1",
        OptionSettings=[
            {
                "Namespace": "aws:autoscaling:launchconfiguration",
                "OptionName": "IamInstanceProfile",
                "Value": "EMR_EC2_DefaultRole",
            },
            {
                "Namespace": "aws:autoscaling:launchconfiguration",
                "OptionName": "EC2KeyName",
                "Value": "shantanu_raj",
            },
            {"Namespace": "aws:autoscaling:asg", "OptionName": "MaxSize", "Value": "2"},
        ],
    )

    print(response)


if __name__ == "__main__":
    # cloudFront_distribution
    create_version()
    time.sleep(5)
    create_environment()
