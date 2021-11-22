import boto3

try:
    client = boto3.client("elasticbeanstalk")
    response = client.create_application(
        ApplicationName="Web-App-trial-a0",
    )

    client.create_application_version(
        ApplicationName="Web-App-trial-a0",
        VersionLabel="v1",
        SourceBundle={
            "S3Bucket": "cloud-1901183-lab4",
            "S3Key": "mysite.zip",
        },
    )

    client.create_environment(
        ApplicationName="Web-App-trial-a0",
        EnvironmentName="Web-App-env-trial-a0",
        Tier={
            "Name": "WebServer",
            "Type": "Standard",
        },
        SolutionStackName="64bit Amazon Linux 2 v3.3.5 running PHP 8.0",
        VersionLabel="v1",
        OptionSettings=[
            {
                "Namespace": "aws:autoscaling:launchconfiguration",
                "OptionName": "IamInstanceProfile",
                "Value": "aws-elasticbeanstalk-ec2-role",
            },
        ],
    )
    print(response)
except Exception as e:
    print(e)
