# helper method for extracting data of the player
import requests
from bs4 import BeautifulSoup


def extract_info(tr):
    base = "https://sofifa.com/"
    link = base + tr.select('td.col-name')[0].find("a").get("href")
    return {
        "name": tr.select('td.col-name')[0].find("a").get("aria-label"),
        "country": tr.select('td.col-name')[0].find("img").get("title"),
        "age": tr.select('td.col.col-ae')[0].text.strip(),
        "overall": tr.select('td.col.col-oa')[0].text.strip(),
        "potential": tr.select('td.col.col-pt')[0].text.strip(),
        "club": tr.select("td.col-name")[1].find("a").text,
        "best_position": tr.select('td.col-name')[0].find("span").text,
        "value": tr.select('td.col.col-vl')[0].text.strip(),
        "wage": tr.select('td.col.col-wg')[0].text.strip(),
        "stats": extract_stats(link)
    }
    

# helper method for extracting stats of single player

def extract_stats(link):
    new_res = requests.get(link)
    new_soup = BeautifulSoup(new_res.content, "html.parser")
    new_tbody = new_soup.find_all("div", {"class": "center"})[5]
    stats_block = new_tbody.findAll("div", {"class": "block-quarter"})
    return extract_deep(stats_block)


def extract_deep(stats_block):
    return {"Att": extract_att(stats_block[0].find("ul")),
            "Skill": extract_skill(stats_block[1].find("ul")),
            "Move": extract_move(stats_block[2].find("ul")),
            "Power": extract_pow(stats_block[3].find("ul")),
            "Mentality": extract_mentality(stats_block[4].find("ul")),
            "Defending": extract_def(stats_block[5].find("ul")),
            "Goalkeep": extract_goalkeep(stats_block[6].find("ul"))}


# helpers for extract_deep(tr)
def extract_att(att):
    return {"Crossing": att.select("li")[0].find("span").text.strip(),
            "Finishing": att.select("li")[1].find("span").text.strip(),
            "Heading Accuracy":  att.select("li")[2].find("span").text.strip(),
            "Short passing": att.select("li")[3].find("span").text.strip()
            #"Volleys": att.select("li")[4].find("span").text.strip()
            }


def extract_skill(ski):
    return {"Dribbling": ski.select("li")[0].find("span").text.strip(),
            "Curve": ski.select("li")[1].find("span").text.strip(),
            "Fk Accuracy": ski.select("li")[2].find("span").text.strip(),
            "Long Passing": ski.select("li")[3].find("span").text.strip(),
            "Ball Control": ski.select("li")[4].find("span").text.strip()
            }


def extract_move(mov):
    return {"Acceleration": mov.select("li")[0].find("span").text.strip(),
            "Sprint Speed": mov.select("li")[1].find("span").text.strip(),
            "Agility": mov.select("li")[2].find("span").text.strip(),
            "Reactions": mov.select("li")[3].find("span").text.strip(),
            "Balance": mov.select("li")[4].find("span").text.strip()
            }


def extract_pow(pow):
    return {"Shot Power": pow.select("li")[0].find("span").text.strip(),
            "Jumping": pow.select("li")[1].find("span").text.strip(),
            "Stamina": pow.select("li")[2].find("span").text.strip(),
            "Strength": pow.select("li")[3].find("span").text.strip(),
            "Long Shots": pow.select("li")[4].find("span").text.strip()
            }


def extract_mentality(men):
    return {"Aggression": men.select("li")[0].find("span").text.strip(),
            "Interceptions": men.select("li")[1].find("span").text.strip(),
            "Positioning": men.select("li")[2].find("span").text.strip(),
            "Vision": men.select("li")[3].find("span").text.strip(),
            "Penalties": men.select("li")[4].find("span").text.strip()
            #"Composure": men.select("li")[5].find("span").text.strip()
            }


def extract_def(defe):
    return {"Marking": defe.select("li")[0].find("span").text.strip(),
            "Standing Tackle": defe.select("li")[1].find("span").text.strip(),
            "Sliding Tackle": defe.select("li")[2].find("span").text.strip()
            }


def extract_goalkeep(gk):
    return {"Diving": gk.select("li")[0].find("span").text.strip(),
            "Handling": gk.select("li")[1].find("span").text.strip(),
            "Kicking": gk.select("li")[2].find("span").text.strip(),
            "Positioning": gk.select("li")[3].find("span").text.strip(),
            "Reflexes": gk.select("li")[4].find("span").text.strip()
            }
    
