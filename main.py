import logging
import time

from scraper.scraper import Scraper
from utils.multi_threading import MultiThreading
from utils.save_csv import save_csv
import logging.config


def main():
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("sLogger")

    url = "https://sofifa.com/players?offset="
    urls = []
    for offset in range(0,20040,60):
        try:
            urls.append(url + str(offset))
        except Exception as e:
            print(f"incorrect url passed to array {url}")
            raise e

    # Parameters
    number_of_scraper = 30
    pages = 10

    #scrapers = [Scraper(urls[pages * i:min(pages * (i + 1), len(urls))]) for i in range(number_of_scraper)]

    scrapers = []
    for i in range(number_of_scraper):
        try:
            scrapers.append(Scraper(urls[pages * i:min(pages * (i + 1), len(urls))]))

        except Exception as e:
            print(f"Wrong scraper array, {scrapers[i]}")
            raise e

    # logging the track of scraping
    logger.info("Scraping surface started...")  # considering adding timer to record
    multi_threading = MultiThreading(scrapers)
    multi_threading.run()

    logger.info("Scraping surface finished.")
    time.sleep(1)

    # logging the track of saving csv

    logger.info("Generating surface CSV file...")  # considering adding timer to record
    save_csv(Scraper.players_scraped)
    logger.info("CSV file is generated")


if __name__ == "__main__":
    main()
