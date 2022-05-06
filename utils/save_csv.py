from itertools import chain
import os
import pandas as pd


from utils.pipeline import pipeline


def save_csv(data):
    """
    Save the data scraped to a .csv file
    :param data:
    :return: csv
    """

    df = pd.DataFrame(list(chain.from_iterable(data)))
    pipeline(df)
    outname = "player_raw_data.csv"
    outdir = "./data/raw"
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fullname = os.path.join(outdir, outname)
    df.to_csv(fullname, index=False, encoding='utf-8-sig')

