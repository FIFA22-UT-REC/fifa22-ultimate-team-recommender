# Helper to extract detail stats and attributes of the player (starts another layer of scraping)
import requests
from bs4 import BeautifulSoup
from scraper.stats_utils.extract_deep import extract_deep
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
        new_tbody = new_soup.find_all("div", {"class": "center"})[5]
        stats_block = new_tbody.findAll("div", {"class": "block-quarter"})
        return extract_deep(stats_block)
    except Exception as e:
        print(f"Link incorrect, {link}")
        raise e
