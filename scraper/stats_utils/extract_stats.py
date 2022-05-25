# Helper to extract detail stats and attributes of the player (starts another layer of scraping)
import requests
from bs4 import BeautifulSoup
from extract_deep import extract_deep


def extract_stats(link):
    new_res = requests.get(link)
    new_soup = BeautifulSoup(new_res.content, "html.parser")
    new_tbody = new_soup.find_all("div", {"class": "center"})[5]
    stats_block = new_tbody.findAll("div", {"class": "block-quarter"})
    return extract_deep(stats_block)