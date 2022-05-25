from unittest import TestCase
import requests
from bs4 import BeautifulSoup
from extract_att import extract_att
from extract_def import extract_def
from extract_skill import extract_skill
from extract_pow import extract_pow
from extract_move import extract_move
from extract_mentality import extract_mentality
from extract_goalkeep import extract_goalkeep
from extract_deep import extract_deep


class Test(TestCase):
    def test_extract_deep(self):
        link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
        res = requests.get(link)
        soup = BeautifulSoup(res.content, "html.parser")
        tb = soup.find_all("div", {"class": "center"})[5]
        blocks = tb.findAll("div", {"class": "block-quarter"})
        actual = extract_deep(blocks)
        expected = {"Att": {"Crossing": "34",
                            "Finishing": "48",
                            "Heading Accuracy":  "82",
                            "Short passing": "67",
                            "Volleys": "40"
                            },
                    "Skill": {"Dribbling": "51",
                              "Curve": "38",
                              "Fk Accuracy": "34",
                              "Long Passing": "42",
                              "Ball Control": "74"
                },
                    "Move": {"Acceleration": "59",
                             "Sprint Speed": "65",
                             "Agility": "34",
                             "Reactions": "80",
                             "Balance": "57"
                             },
                    "Power": {"Shot Power": "51",
                              "Jumping": "87",
                              "Stamina": "86",
                              "Strength": "83",
                              "Long Shots": "34"
                              },
                    "Mentality": {"Aggression": "94",
                                  "Interceptions": "82",
                                  "Positioning": "32",
                                  "Vision": "51",
                                  "Penalties": "47",
                                  "Composure": "72"
                                  },
                    "Defending": {"Defensive Awareness": "78",
                                  "Standing Tackle": "81",
                                  "Sliding Tackle": "77"
                                  },
                    "Goalkeep": {"Diving": "13",
                                 "Handling": "12",
                                 "Kicking": "8",
                                 "Positioning": "6",
                                 "Reflexes": "8"
                                 }}

        self.assertEqual(actual, expected)
