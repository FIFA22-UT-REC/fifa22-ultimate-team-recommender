# Helper method to extract movement attributes of the player

def extract_move(mov):
    return {"Acceleration": mov.select("li")[0].find("span").text.strip(),
            "Sprint Speed": mov.select("li")[1].find("span").text.strip(),
            "Agility": mov.select("li")[2].find("span").text.strip(),
            "Reactions": mov.select("li")[3].find("span").text.strip(),
            "Balance": mov.select("li")[4].find("span").text.strip()
            }
