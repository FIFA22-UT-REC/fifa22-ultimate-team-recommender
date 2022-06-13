import boto3


def load_items(players, tbname):
    db = boto3.resource("dynamodb", region_name="us-west-2")
    table = db.Table(tbname)
    for player in players:
        # name = (player["name"])
        # printing info
        # print(f"Loading player: {name}")
        table.put_item(Item=player)