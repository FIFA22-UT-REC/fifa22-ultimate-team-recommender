from unittest import TestCase
import requests
from bs4 import BeautifulSoup
from extract_stats import extract_stats


class Test(TestCase):
    def test_extract_stats(self):
        link = "https://sofifa.com/player/229582/gianluca-mancini/220053/"
        actual = extract_stats(link)
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
