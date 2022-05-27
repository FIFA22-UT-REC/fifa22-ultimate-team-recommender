# Helper method to extract defending attributes of a player

def extract_def(defe):
    getDefe = defe.select("li")
    assert len(getDefe) == 3, f"List out of range {getDefe}"
    return {"Defensive Awareness": getDefe[0].find("span").text.strip(),
            "Standing Tackle": getDefe[1].find("span").text.strip(),
            "Sliding Tackle": getDefe[2].find("span").text.strip()
            }