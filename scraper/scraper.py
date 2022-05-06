from bs4 import BeautifulSoup
import requests
import random
import time
import logging

from scraper.scraper_utlis import extract_info


class Scraper(object):
    """
    Pull player info down from web
    """

    # Initialize array to store player
    players_scraped = []

    # Instantiate scraper
    def __init__(self, urls, user_agent):
        self.urls = urls
        self.headers = {"UserAgent": user_agent}
        self.logger = logging.getLogger("sLogger")

    # request to get the url
    def get_page(self, url, headers):
        response = requests.get(url, headers=headers)
        if response.status_code:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup.find("tbody", {"class": "list"})
        else:
            self.logger.error("Error" + response.status_code)
            return None

    # helper method to get players
    def get_players(self, trs):
        return [extract_info(tr) for tr in trs]

    # method to extract and copy player info from web
    def scrap(self, urls, headers):
        for url in urls:
            tbody = self.get_page(url, headers)
            if tbody is None:
                continue
            trs = tbody.findAll("tr")
            Scraper.players_scraped.append(self.get_players(trs))
            self.logger.info("Page{} scraped".format(len(Scraper.players_scraped)))
            time.sleep(random.randit(3, 8))

    # method to start the scraper
    def start(self):
        self.scrap(self.urls, self.headers)

