from bs4 import BeautifulSoup
import requests
import logging

from scraper.extract_info import extract_info
#from fifa_pack.extract_info import extract_info


class Scraper(object):
    """
    Pull player info down from web
    """
    
    # fix this later, using property instead
    players_scraped = []
    # Instantiate scraper object

    def __init__(self, urls):
        self._urls = urls
        # self._players = []
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
    def get_players(self, trs):
        out = []
        for tr in trs:
            try:
                base = "https://sofifa.com/"
                name = tr.select('td.col-name')
                attr = "?attr=classic"
                p_url = name[0].find("a").get("href")
                a, b, c, d, v = p_url.split("/", 4)
                version = v[0:2]
                if version != "22":
                    continue
                link = base + p_url + attr
                out.append(extract_info(tr, link))
            except Exception as e:
                # print(f"error parsing link, check!")
                self.logger.error(f"error parsing link {link}")
                raise e
        return out

    # method to extract and copy player info from web
    def scrap(self, urls):
        for url in urls:
            tbody = self.get_page(url)
            if tbody is None:
                continue
            trs = tbody.findAll("tr")
            Scraper.players_scraped.append(self.get_players(trs))
            self.logger.info(f"Done for url: {url}")
            self.logger.info("Page{} scraped".format(len(Scraper.players_scraped)))
        #self._players = Scraper.players_scraped

    # method to start the scraper
    def start(self):
        self.scrap(self._urls)

    #@property
    #def player_data(self):
    #    return self._players

    @property
    def urls(self):
        return self._urls


