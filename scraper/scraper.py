from bs4 import BeautifulSoup
import requests
import random
import time
import logging

from scraper.extract_info import extract_info


class Scraper(object):
    """
    Pull player info down from web
    """

    # Initialize array to store player
    players_scraped = []

    # Instantiate scraper
    def __init__(self, urls):
        self.urls = urls
        self.logger = logging.getLogger("sLogger")

    # request to get the url
    def get_page(self, url):
        response = requests.get(url)
        if response.status_code:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup.find("tbody", {"class": "list"})
        else:
            self.logger.error("Error" + response.status_code)
            return None

    # helper method to get players
    def get_players(self,trs):
        return [extract_info(tr) for tr in trs]

    # method to extract and copy player info from web
    def scrap(self, urls):
        for url in urls:
            tbody = self.get_page(url)
            if tbody is None:
                continue
            trs = tbody.findAll("tr")
            Scraper.players_scraped.append(self.get_players(trs))
            self.logger.info("Page{} scraped".format(len(Scraper.players_scraped)))

    # method to start the scraper
    def start(self):
        self.scrap(self.urls)

