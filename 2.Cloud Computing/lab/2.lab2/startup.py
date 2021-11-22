import boto3

client = boto3.resource('ec2', region_name='us-east-1')

startupscript = open(r"D:\useful\sem 5\2.cloud computing\lab\2.lab2\script.sh","r")
bucketFiles=startupscript.read()

Myinstances = client.create_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'gp2'
            },
        },
    ],
    ImageId='ami-0c2b8ca1dad447f8a',
    InstanceType='t2.micro',
    KeyName='shantanu_raj',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
    SecurityGroupIds=[
        'sg-0e111f2c98c14c3a5',
    ],
    UserData=bucketFiles,
   
)
instance=Myinstances[0]
print("New instance of EC2 is created",instance.id)
print(instance)
instance.wait_until_running()
print("running state")               
print(client.Instance(instance.id).public_dns_name)