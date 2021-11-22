import boto3


# aws configuration
#access_id_key = "ASIA3REMKRJ4GCR4WBOT"
#secret_access_key = "RdCeghkaSkgnZHzBHWMvr7n9KyeTrtOGS2Iw67iQ"
#session_token_key = "FwoGZXIvYXdzEK7//////////wEaDPK+UUSHHZZ5EqH8FSLIAUsdRlZAOW0UFXWx76vledxBwBIIsgt3O9jFdkXEczOqodEir1n36N8DjK0eDTDOsXOt8dum1SvQsyxwUmaxkq1bcbsfbXGmXhsK+XTVc4N1ReiLFhbVhq9qwBYlJOVl9j1c5xS/5mkP7UIUC8G/q/QY/CqiT7lbTC/7ua788nrLAAFTyK54Ufgg7tMyNAScTx3pOc+zxkdecbnOlA7DlAnHe2YoVD7UZ0CG5aOT8uMEgAbR23FUn4YKH2bKhX9WcXqHdJZd6beeKKj5qIoGMi3y5SCXd1XqcPPax0Hoe3o4srAMKiZV4eaQkkbKAHP87pqpUZstNktGdidxnPs="


rdsClient = boto3.client(
    "rds",
    #aws_access_key_id=access_id_key,
    #aws_secret_access_key=secret_access_key,
    #aws_session_token=session_token_key,
    #region_name="us-east-1",
)

response = rdsClient.create_db_instance(
    DBName="TestDb1",
    DBInstanceIdentifier="database-1",
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    Engine="MySQL",
    MasterUsername="root",
    MasterUserPassword="root0000",
    PubliclyAccessible=True,
)


import time

while True:
    response = rdsClient.describe_db_instances(
        DBInstanceIdentifier="database-1",
        MaxRecords=20,
    )

    status = response["DBInstances"][0]["DBInstanceStatus"]

    if status == "available" or status == "AVAILABLE":
        break
    else:
        time.sleep(10)


print(response["DBInstances"][0]["Endpoint"]["Address"])
