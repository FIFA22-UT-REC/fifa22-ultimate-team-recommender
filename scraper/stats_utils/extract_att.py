# Helper method to extract attacking attributes of the player

def extract_att(att):
    getAtt = att.select("li")
    assert len(getAtt) == 5, f"List out of range {getAtt}"
    return {"Crossing": getAtt[0].find("span").text.strip(),
            "Finishing": getAtt[1].find("span").text.strip(),
            "Heading Accuracy":  getAtt[2].find("span").text.strip(),
            "Short passing": getAtt[3].find("span").text.strip(),
            "Volleys": getAtt[4].find("span").text.strip()
            }
