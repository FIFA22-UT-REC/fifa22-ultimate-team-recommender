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
        "stats" : extract_stats(link)
    }
    

# helper method for extracting stats of single player

def extract_stats(link):
    new_res = requests.get(link)
    new_soup = BeautifulSoup(new_res.content, "html.parser")
    n_tbody = new_soup.find_all("div", {"class":"center"})[5]
    stats_block = n_tbody.findAll("div", {"class":"block-quarter"})
    return extract_deep(stats_block)

def extract_deep(tr):
    return {"Att": extract_att(tr[0]) 
        , "Skill" : extract_skill(tr[1]) 
        , "Move" : extract_move(tr[2])
        , "Power" : extract_pow(tr[3])
        , "Mentality" : extract_mentality(tr[4])
        , "Defending" : extract_def(tr[5])
        , "Goalkeep" : extract_goalkeep(tr[6])}


# helpers for extract_deep(tr)
def extract_att(tr):
    return {"Crossing" : tr.findAll("li")[0].find("span").text.strip(),
           "Finishing" : tr.findAll("li")[1].find("span").text.strip(),
           "Heading Accuracy":  tr.findAll("li")[2].find("span").text.strip(),
           "Short passing":tr.findAll("li")[3].find("span").text.strip(),
           "Volleys": tr.findAll("li")[4].find("span").text.strip()
            }

def extract_skill(tr):
    return {"Dribbling" : tr.findAll("li")[0].find("span").text.strip(),
           "Curve" : tr.findAll("li")[1].find("span").text.strip(),
           "Fk Accuracy": tr.findAll("li")[2].find("span").text.strip(),
           "Long Passing": tr.findAll("li")[3].find("span").text.strip(),
           "Ball Control": tr.findAll("li")[4].find("span").text.strip()
            }

def extract_move(tr):
    return {"Acceleration" : tr.findAll("li")[0].find("span").text.strip(),
           "Sprint Speed" : tr.findAll("li")[1].find("span").text.strip(),
           "Agility": tr.findAll("li")[2].find("span").text.strip(),
           "Reactions": tr.findAll("li")[3].find("span").text.strip(),
           "Balance": tr.findAll("li")[4].find("span").text.strip()
            }

def extract_pow(tr):
    return {"Shot Power" : tr.findAll("li")[0].find("span").text.strip(),
           "Jumping" : tr.findAll("li")[1].find("span").text.strip(),
           "Stamina": tr.findAll("li")[2].find("span").text.strip(),
           "Strength": tr.findAll("li")[3].find("span").text.strip(),
           "Long Shots": tr.findAll("li")[4].find("span").text.strip()
            }

def extract_mentality(tr):
    return {"Aggression" : tr.findAll("li")[0].find("span").text.strip(),
           "Interceptions" : tr.findAll("li")[1].find("span").text.strip(),
           "Positioning": tr.findAll("li")[2].find("span").text.strip(),
           "Vision": tr.findAll("li")[3].find("span").text.strip(),
           "Penalties": tr.findAll("li")[4].find("span").text.strip(),
           "Composure": tr.findAll("li")[5].find("span").text.strip()
            }

def extract_def(tr):
    return {"Defensive Awareness" : tr.findAll("li")[0].find("span").text.strip(),
           "Standing Tackle" : tr.findAll("li")[1].find("span").text.strip(),
           "Sliding Tackle": tr.findAll("li")[2].find("span").text.strip()
            }

def extract_goalkeep(tr):
    return {"Diving" : tr.findAll("li")[0].find("span").text.strip(),
           "Handling" : tr.findAll("li")[1].find("span").text.strip(),
           "Kicking": tr.findAll("li")[2].find("span").text.strip(),
           "Positioning": tr.findAll("li")[3].find("span").text.strip(),
           "Reflexes": tr.findAll("li")[4].find("span").text.strip()
            }
    

    
    
    