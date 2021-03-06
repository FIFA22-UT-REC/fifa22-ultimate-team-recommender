import logging
import time

from scraper.scraper import Scraper
from utils.multi_threading import MultiThreading
from utils.save_data import save_data
import logging.config


def main():
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("sLogger")

    url = "https://sofifa.com/players?offset="
    urls = []
    for offset in range(0, 20060, 60):
        try:
            urls.append(url + str(offset))
        except Exception as e:
            print(f"incorrect url passed to array {url}")
            raise e

    # Parameters
    number_of_scraper = 30
    pages = 10

    # scrapers = [Scraper(urls[pages * i:min(10 * (i + 1), len(urls))]) for i in range(number_of_scraper)]
    #print(Scraper.players_scraped)
    

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
    t1 = time.time()

    # logging the track of saving csv

    logger.info("Generating surface CSV file...")  # considering adding timer to record
    logger.info("Generating json and uploading to dynamo database...")

    dat = Scraper.players_scraped
    # logger.info(f"As a property : {type(dat)}, {dat}")
    save_data(dat)
    logger.info("CSV file is generated")
    logger.info("json file is generated")
    logger.info(f"Total time to scrap and save was: {time.time() - t1} s")
    print("Done!, Check the logger")


if __name__ == "__main__":
    main()
