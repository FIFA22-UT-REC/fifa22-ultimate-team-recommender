from itertools import chain
import pandas as pd

from utils.pipeline import pipeline


def flat(data):
    """
    helper method to convert columns to rows observations of player
    :param object:
    :return:
    """
    list(chain.from_iterable(data))


def save_csv(data):
    """
    Save the data scraped to a .csv file
    :param data:
    :return: csv
    """

    df = pd.DataFrame(flat(data))
    pipeline(df)
    df.to_csv("./data/fifa22.csv", index=False, encoding='utf-8-sig')

