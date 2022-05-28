from unittest import TestCase
import requests
from bs4 import BeautifulSoup
from extract_def import extract_def


class Test(TestCase):
    def test_extract_def(self):
        link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
        res = requests.get(link)
        soup = BeautifulSoup(res.content,"html.parser")
        tb = soup.find_all("div", {"class": "center"})[5]
        blo = tb.findAll("div", {"class": "block-quarter"})
        defe = blo[5]
        actual = extract_def(defe)
        expected = {"Defensive Awareness": "78",
                    "Standing Tackle": "81",
                    "Sliding Tackle": "77"
                    }

        self.assertEqual(actual, expected)

