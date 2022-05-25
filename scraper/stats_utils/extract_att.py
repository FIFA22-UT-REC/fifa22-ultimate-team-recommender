# Helper method to extract attacking attributes of the player

def extract_att(att):
    return {"Crossing": att.select("li")[0].find("span").text.strip(),
            "Finishing": att.select("li")[1].find("span").text.strip(),
            "Heading Accuracy":  att.select("li")[2].find("span").text.strip(),
            "Short passing": att.select("li")[3].find("span").text.strip(),
            "Volleys": att.select("li")[4].find("span").text.strip()
            }
