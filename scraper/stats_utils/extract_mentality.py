# Helper method to extract mentality traits of the player

def extract_mentality(men):
    return {"Aggression": men.select("li")[0].find("span").text.strip(),
            "Interceptions": men.select("li")[1].find("span").text.strip(),
            "Positioning": men.select("li")[2].find("span").text.strip(),
            "Vision": men.select("li")[3].find("span").text.strip(),
            "Penalties": men.select("li")[4].find("span").text.strip(),
            "Composure": men.select("li")[5].find("span").text.strip()
            }