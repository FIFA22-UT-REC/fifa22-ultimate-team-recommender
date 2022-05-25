# helper method for extracting data of the player
import requests
from bs4 import BeautifulSoup
from stats_utils.extract_goalkeep import extract_goalkeep
from stats_utils.extract_def import extract_def


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









