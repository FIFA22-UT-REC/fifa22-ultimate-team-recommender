from itertools import chain
import pandas as pd

from utils.pipeline import pipeline


def save_csv(data):
    """
    Save the data scraped to a .csv file
    :param data:
    :return: csv
    """

    flatten = lambda x: list(chain.from_iterable(x))

    df = pd.DataFrame(flatten(data))
    df = pipeline(df)
    df.to_csv("./data/fifa22.csv", index=False, encoding='utf-8-sig')

