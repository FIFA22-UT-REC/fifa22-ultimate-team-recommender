# Helper to extract detail stats and attributes of the player (starts another layer of scraping)
import requests
from bs4 import BeautifulSoup
from fifa_pack.extract_deep import extract_deep
import logging

def extract_stats(link):
    try:
        new_res = requests.get(link)
        new_soup = BeautifulSoup(new_res.content, "html.parser")
        try:
            version = new_soup.find("span", {"class": "bp3-button-text"}).text
            assert version == "FIFA 22"
        except Exception as e:
            print(f"Wrong version of FIFA, {version}")
            raise e
        stats_block = new_soup.find_all("div", {"class": "center"})[5].findAll("div", {"class": "block-quarter"})
        profile = new_soup.findAll("div", {"class": "col-12"})[0].findAll("div", {"class":"block-quarter"})[4].find("ul").findAll("li")
        metrics = new_soup.findAll("")
        return {"preferred_foot" : profile[0].text.split()[1][4:],
            "weak_foot" : profile[1].text.split()[0],
            "skill_move": profile[2].text.split()[0],
            "work_rate" : profile[4].text.strip()[9:],
            "attrs": extract_deep(stats_block)
            }
    except Exception as e:
        print(f"Link incorrect, {link}")
        raise e
