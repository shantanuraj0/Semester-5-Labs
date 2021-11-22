import boto3

ebsClient = boto3.client('elasticbeanstalk')

version_label = 'version_demo'
application_name = 'MyHomePage'
environment_name = 'MyHomePageEnv'


def createNewVersion():
    try:
        ebsClient.create_application_version(
            ApplicationName=application_name,
            VersionLabel=version_label,
            Description='Portfolio website',
            SourceBundle={
                'S3Bucket': 'cloud-1901183-lab4',
                'S3Key': 'portfolio.zip'
            },
            AutoCreateApplication=True,
            Process=False
        )
        print('application Created')
    except Exception as e:
        print('some error has occured: ', e)


def createEnvironment():
    try:
        ebsClient.create_environment(
            ApplicationName=application_name,
            EnvironmentName=environment_name,
            Description='Portfolio web app Nodejs environment',
            CNAMEPrefix='Sraj',
            Tier={
                'Name': 'WebServer',
                'Type': 'Standard',
            },
            VersionLabel=version_label,
            SolutionStackName='64bit Amazon Linux 2 v3.3.5 running PHP 8.0',
            OptionSettings=[
                {
                    'Namespace': 'aws:autoscaling:launchconfiguration',
                    'OptionName': 'IamInstanceProfile',
                    'Value': 'aws-elasticbeanstalk-ec2-role'
                },
            ],
        )
        print('Environment Created')
    except Exception as e:
        print('some error has occured: ', e)


def init():
    createNewVersion()
    createEnvironment()


if __name__ == '__main__':
    init()
