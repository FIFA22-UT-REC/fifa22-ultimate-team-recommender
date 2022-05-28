from unittest import TestCase
import requests
from bs4 import BeautifulSoup
from extract_att import extract_att


class Test(TestCase):
    def test_extract_att(self):
        link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
        res = requests.get(link)
        soup = BeautifulSoup(res.content, "html.parser")
        tb = soup.find_all("div", {"class": "center"})[5]
        blo = tb.findAll("div", {"class": "block-quarter"})
        att = blo[0]
        actual = extract_att(att)
        expected = {"Crossing": "34",
                    "Finishing": "48",
                    "Heading Accuracy":  "82",
                    "Short passing": "67",
                    "Volleys": "40"
                    }
        self.assertEqual(actual, expected)

