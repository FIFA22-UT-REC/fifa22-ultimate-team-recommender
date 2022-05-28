from unittest import TestCase
import requests
from bs4 import BeautifulSoup
from extract_move import extract_move


class Test(TestCase):
    def test_extract_move(self):
        link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
        res = requests.get(link)
        soup = BeautifulSoup(res.content, "html.parser")
        tb = soup.find_all("div", {"class": "center"})[5]
        blo = tb.findAll("div", {"class": "block-quarter"})
        mov = blo[2]
        actual = extract_move(mov)
        expected = {"Acceleration": "59",
                    "Sprint Speed": "65",
                    "Agility": "34",
                    "Reactions": "80",
                    "Balance": "57"
                    }
        self.assertEqual(actual, expected)

