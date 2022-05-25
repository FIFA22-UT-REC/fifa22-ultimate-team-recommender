# Helper method to extract gk attributes of player

def extract_goalkeep(gk):
    return {"Diving": gk.select("li")[0].find("span").text.strip(),
            "Handling": gk.select("li")[1].find("span").text.strip(),
            "Kicking": gk.select("li")[2].find("span").text.strip(),
            "Positioning": gk.select("li")[3].find("span").text.strip(),
            "Reflexes": gk.select("li")[4].find("span").text.strip()
            }
    