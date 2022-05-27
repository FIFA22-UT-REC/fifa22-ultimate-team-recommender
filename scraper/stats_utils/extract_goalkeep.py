# Helper method to extract gk attributes of player

def extract_goalkeep(gk):
    getGk = gk.select("li")
    assert len(getGk) == 5, f"List out of range {getGk}"
    return {"Diving": getGk[0].find("span").text.strip(),
            "Handling": getGk[1].find("span").text.strip(),
            "Kicking": getGk[2].find("span").text.strip(),
            "Positioning": getGk[3].find("span").text.strip(),
            "Reflexes": getGk[4].find("span").text.strip()
            }
    