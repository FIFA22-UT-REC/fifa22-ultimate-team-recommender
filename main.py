import logging
import time

from scraper.scraper import Scraper
from utils.multi_threading import MultiThreading
from utils.save_csv import save_csv
import logging.config


def main():

    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("sLogger")


    params = {
        "ae": "0",
        "oa": "1",
        "pt": "2",
        "vl": "3",
        "wg": "4",
        #"pf": "5",
        #"hi": "6",
        #"wi": "7",
        "bp": "8",
        #"pac": "9",
        #"pas": "10",
        #"sho": "11",
        #"phy": "12",
        #"dri": "13",
        #"def": "14"
    }

    query = "&".join([f"showCol%5B{y}%5D={x}" for x, y in params.items()])
    url = f"https://sofifa.com/players?{query}&offset="
    urls = [url + str(offset) for offset in range(0, 120, 60)]

    # Parameters
    number_of_scraper = 31
    pages = 10

    scrapers = [Scraper(urls[pages*i:min(pages*(i+1), len(urls))]) for i in range(number_of_scraper)]

    # logging the track of scraping
    logger.info("Scraping started...")     # considering adding timer to record
    multi_threading = MultiThreading(scrapers)
    multi_threading.run()
    logger.info("Scraping finished.")
    time.sleep(1)
    # logging the track of saving csv
    logger.info("Generating CSV file...")   # considering adding timer to record
    save_csv(Scraper.players_scraped)
    logger.info("CSV file is generated.")


if __name__ == "__main__":
    main()
