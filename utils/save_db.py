import boto3
from utils.load_items import load_items


def save_db(players, tbname, save):
    # connects to the database as client
    dynamodb_cli = boto3.client("dynamodb", region_name="us-west-2")
    # get names of all tables on AWS cloud
    existing_tables = dynamodb_cli.list_tables()["TableNames"]
    # check if table have created or not
    if tbname not in existing_tables:
        dynamodb_cli.create_table(
            TableName=tbname,
            KeySchema=[
                {
                        'AttributeName': 'name', # This could change
                        'KeyType': 'HASH'  # Partition key
                },
                {
                        'AttributeName': 'country', # This could change
                        'KeyType': 'RANGE'  # Sort key
                }
                ],
            AttributeDefinitions=[
                    {
                        'AttributeName': 'name',
                        # AttributeType defines the data type. 'S' is string type and 'N' is number type
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'country',
                        'AttributeType': 'S'
                    },
                ],
            ProvisionedThroughput={
                    # ReadCapacityUnits set to 10 strongly consistent reads per second
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10  # WriteCapacityUnits set to 10 writes per second
                }
            )
        # Checks to wait table created
        dynamodb_cli.get_waiter('table_exists').wait(TableName=tbname)

        # Once table exists load the data into database
        load_items(players=players, tbname=tbname)

    # add a logger info here to notify table already exists
    # saves the player
    load_items(players=players, tbname=tbname)