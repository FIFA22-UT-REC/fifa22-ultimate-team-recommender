# Helper method to extract defending attributes of a player

def extract_def(defe):
    return {"Defensive Awareness": defe.select("li")[0].find("span").text.strip(),
            "Standing Tackle": defe.select("li")[1].find("span").text.strip(),
            "Sliding Tackle": defe.select("li")[2].find("span").text.strip()
            }