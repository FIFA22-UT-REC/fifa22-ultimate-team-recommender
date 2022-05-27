# Helper method to extract power attributes of the player

def extract_pow(pow):

    getPow = pow.select("li")
    assert len(getPow) == 5, f"List out of range {getPow}"
    return {"Shot Power": getPow[0].find("span").text.strip(),
            "Jumping": getPow[1].find("span").text.strip(),
            "Stamina": getPow[2].find("span").text.strip(),
            "Strength": getPow[3].find("span").text.strip(),
            "Long Shots": getPow[4].find("span").text.strip()
            }