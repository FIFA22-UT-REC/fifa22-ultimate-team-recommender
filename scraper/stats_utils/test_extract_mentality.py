from unittest import TestCase
import requests
from bs4 import BeautifulSoup
from extract_mentality import extract_mentality


class Test(TestCase):
    def test_extract_mentality(self):
        link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
        res = requests.get(link)
        soup = BeautifulSoup(res.content,"html.parser")
        tb = soup.find_all("div", {"class": "center"})[5]
        blo = tb.findAll("div", {"class": "block-quarter"})
        men = blo[4]
        actual = extract_mentality(men)
        expected = {"Aggression": "94",
                    "Interceptions": "82",
                    "Positioning": "32",
                    "Vision": "51",
                    "Penalties": "47",
                    "Composure": "72"
                    }
        self.assertEqual(actual, expected)
