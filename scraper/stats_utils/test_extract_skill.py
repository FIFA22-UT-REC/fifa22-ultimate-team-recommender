from unittest import TestCase
import requests
from bs4 import BeautifulSoup


def test_extract_skill(self):
    link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
    res = requests.get(link)
    soup = BeautifulSoup(res.content, "html.parser")
    tb = soup.find_all("div", {"class": "center"})[5]
    blo = tb.findAll("div", {"class": "block-quarter"})
    ski = blo[1]
    actual = extract_skill(ski)
    expected = {"Dribbling": "51",
                "Curve": "38",
                "Fk Accuracy": "34",
                "Long Passing": "42",
                "Ball Control": "74"
                }
    self.assertEqual(actual, expected)
