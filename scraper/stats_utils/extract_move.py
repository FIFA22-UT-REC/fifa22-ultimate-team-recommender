# Helper method to extract movement attributes of the player

def extract_move(mov):

    getMov = mov.select("li")
    assert len(getMov) == 5, f"List out of range {getMov}"
    return {"Acceleration": getMov[0].find("span").text.strip(),
            "Sprint Speed": getMov[1].find("span").text.strip(),
            "Agility": getMov[2].find("span").text.strip(),
            "Reactions": getMov[3].find("span").text.strip(),
            "Balance": getMov[4].find("span").text.strip()
            }
