# Helper method to extract power attributes of the player

def extract_pow(pow):
    return {"Shot Power": pow.select("li")[0].find("span").text.strip(),
            "Jumping": pow.select("li")[1].find("span").text.strip(),
            "Stamina": pow.select("li")[2].find("span").text.strip(),
            "Strength": pow.select("li")[3].find("span").text.strip(),
            "Long Shots": pow.select("li")[4].find("span").text.strip()
            }