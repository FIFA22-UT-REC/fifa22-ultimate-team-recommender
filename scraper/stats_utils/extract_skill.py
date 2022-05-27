# Helper method to extract skill attributes of the player

def extract_skill(ski):
    getSki = ski.select("li")
    assert len(getSki) == 5, f"List out of range {getSki}"
    return {"Dribbling": getSki[0].find("span").text.strip(),
            "Curve": getSki[1].find("span").text.strip(),
            "Fk Accuracy": getSki[2].find("span").text.strip(),
            "Long Passing": getSki[3].find("span").text.strip(),
            "Ball Control": getSki[4].find("span").text.strip()
            }
