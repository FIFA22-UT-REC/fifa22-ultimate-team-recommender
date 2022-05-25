from unittest import TestCase
import requests
from bs4 import BeautifulSoup
from extract_goalkeep import extract_goalkeep


class Test(TestCase):
    def test_extract_goalkeep(self):
        link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
        res = requests.get(link)
        soup = BeautifulSoup(res.content,"html.parser")
        tb = soup.find_all("div", {"class": "center"})[5]
        blo = tb.findAll("div", {"class": "block-quarter"})
        gk = blo[6]
        actual = extract_goalkeep(gk)
        expected = {"Diving": "13",
                    "Handling": "12",
                    "Kicking": "8",
                    "Positioning": "6",
                    "Reflexes": "8"
                    }
        self.assertEqual(actual, expected)


