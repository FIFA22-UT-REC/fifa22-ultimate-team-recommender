import logging
import time

from scraper.scraper import Scraper
from utils.multi_threading import MultiThreading
from utils.save_data import save_data
import logging.config
from argparse import ArgumentParser

# Gets command line argument to wheter stop saving to db or not
# And has argument to control number of pages to scrape (each page has 60 players)

# TODO: abstract this to another file as an CLI argument parser
parser = ArgumentParser()
parser.add_argument("-s", "--save")
parser.add_argument("-n", "--number")
args = vars(parser.parse_args())

SAVE_OPTION = args["save"]
NUM = args["number"]

if SAVE_OPTION in ["yes", "Yes", "YES", "y"]:
    SAVE_OPTION = True
else:
    SAVE_OPTION = False


def main(NUM, SAVE_OPTION=False):
    logging.config.fileConfig("logging.conf")
    logger = logging.getLogger("sLogger")

    url = "https://sofifa.com/players?offset="
    urls = []
    
    # print(NUM, type(NUM))
    for offset in range(0, int(NUM), 60):
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
    save_data(dat, save=SAVE_OPTION)
    logger.info("CSV file is generated")
    logger.info("json file is generated")
    logger.info(f"Total time to scrap and save was: {time.time() - t1} s")
    print("Done!, Check the logger")


if __name__ == "__main__":
    main(SAVE_OPTION=SAVE_OPTION, NUM=NUM)
