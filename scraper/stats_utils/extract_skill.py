# Helper method to extract skill attributes of the player

def extract_skill(ski):
    return {"Dribbling": ski.select("li")[0].find("span").text.strip(),
            "Curve": ski.select("li")[1].find("span").text.strip(),
            "Fk Accuracy": ski.select("li")[2].find("span").text.strip(),
            "Long Passing": ski.select("li")[3].find("span").text.strip(),
            "Ball Control": ski.select("li")[4].find("span").text.strip()
            }
