# Helper functions to save the json format data to cloud dynamo database
import boto3
import json

def save_db(jsonDat, tb_name):
    dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
    table = dynamodb.Table(tb_name)
    #n = 0
    with open(jsonDat, "r", encoding="utf-8") as json_file:
        players = json.load(json_file)
        for player in players:
            name = player["name"]
            country = player["country"]
            age = player["age"]
            overall = player["overall"]
            potential = player["potential"]
            club = player["club"]
            best_position = player["best_position"]
            value = player["value"]
            wage = player["wage"]
            preferred_foot = player["preferred_foot"]
            weak_foot = player["weak_foot"]
            skill_move = player["skill_move"]
            work_rate = player["work_rate"]
            Crossing = player["Crossing"]
            Finishing = player["Finishing"]
            Heading_accuracy = player["Heading Accuracy"]
            Short_passing = player["Short passing"]
            Volleys = player["Volleys"]
            Dribbling = player["Dribbling"]
            Curve = player["Curve"]
            Fk_Accuracy = player["Fk Accuracy"]
            Long_Passing = player["Long Passing"]
            Ball_Control = player["Ball Control"]
            Acceleration = player["Acceleration"]
            Sprint_Speed = player["Sprint Speed"]
            Agility = player["Agility"]
            Reactions = player["Reactions"]
            Balance = player["Balance"]
            Shot_Power = player["Shot Power"]
            Jumping = player["Jumping"]
            Stamina = player["Stamina"]
            Strength = player["Strength"]
            Long_Shots = player["Long Shots"]
            Aggression = player["Aggression"]
            Interceptions = player["Interceptions"]
            Positioning = player["Positioning"]
            Vision = player["Vision"]
            Penalties = player["Penalties"]
            Composure = player["Composure"]
            Defensive_Awareness = player["Defensive Awareness"]
            Standing_Tackle = player["Standing Tackle"]
            Sliding_Tackle = player["Sliding Tackle"]
            Diving = player["Diving"]
            Handling = player["Handling"]
            Kicking = player["Kicking"]
            Reflexes = player["Reflexes"]
            #n = n + 1
            #print("Adding detail: ", name, club, n)

            table.put_item(
                Item={
                    "name": name,
                    "country": country,
                    "age": age,
                    "overall": overall,
                    "potential": potential,
                    "club": club,
                    "best_position": best_position,
                    "value": value,
                    "wage": wage,
                    "preferred_foot" : preferred_foot,
                    "weak_foot" : weak_foot,
                    "skill_move" : skill_move,
                    "work_rate" : work_rate,
                    "Crossing": Crossing,
                    "Finishing": Finishing,
                    "Heading Accuracy": Heading_accuracy,
                    "Short passing": Short_passing,
                    "Volleys": Volleys,
                    "Dribbling": Dribbling,
                    "Curve": Curve,
                    "Fk Accuracy": Fk_Accuracy,
                    "Long Passing": Long_Passing,
                    "Ball Control": Ball_Control,
                    "Acceleration": Acceleration,
                    "Sprint Speed": Sprint_Speed,
                    "Agility": Agility,
                    "Reactions": Reactions,
                    "Balance": Balance,
                    "Shot Power": Shot_Power,
                    "Jumping": Jumping,
                    "Stamina": Stamina,
                    "Strength": Strength,
                    "Long Shots": Long_Shots,
                    "Aggression": Aggression,
                    "Interceptions": Interceptions,
                    "Positioning": Positioning,
                    "Vision": Vision,
                    "Penalties": Penalties,
                    "Composure": Composure,
                    "Defensive Awareness": Defensive_Awareness,
                    "Standing Tackle": Standing_Tackle,
                    "Sliding Tackle": Sliding_Tackle,
                    "Diving": Diving,
                    "Handling": Handling,
                    "Kicking": Kicking,
                    "Reflexes": Reflexes
                }
            )