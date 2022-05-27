# Helper method to extract mentality traits of the player

def extract_mentality(men):
    getMen = men.select("li")
    assert len(getMen) == 6, f"List out of range {getMen}"
    return {"Aggression": getMen[0].find("span").text.strip(),
            "Interceptions": getMen[1].find("span").text.strip(),
            "Positioning": getMen[2].find("span").text.strip(),
            "Vision": getMen[3].find("span").text.strip(),
            "Penalties": getMen[4].find("span").text.strip(),
            "Composure": getMen[5].find("span").text.strip()
            }