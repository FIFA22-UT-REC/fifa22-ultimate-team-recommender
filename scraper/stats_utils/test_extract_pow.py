from unittest import TestCase
import requests
from bs4 import BeautifulSoup
from extract_pow import extract_pow


class Test(TestCase):
    def test_extract_pow(self):
        link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
        res = requests.get(link)
        soup = BeautifulSoup(res.content,"html.parser")
        tb = soup.find_all("div", {"class": "center"})[5]
        blo = tb.findAll("div", {"class": "block-quarter"})
        pow = blo[3]
        actual = extract_pow(pow)
        expected = {"Shot Power": "51",
                    "Jumping": "87",
                    "Stamina": "86",
                    "Strength": "83",
                    "Long Shots": "34"
                    }
        self.assertEqual(actual, expected)
