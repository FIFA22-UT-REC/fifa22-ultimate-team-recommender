from itertools import chain
import os
import pandas as pd
import json


from utils.pipeline import pipeline
from utils.flatten import flatten
from utils.save_db import save_db


def save_data(data):
    """
    Save the data scraped to a .csv file
    :param data:
    :return: csv
    """
    
    # Define variables and directories to store data
    outname_csv = "player_raw_data.csv"
    outname_json = "player_raw_data.json"
    outdir = "./data/raw"
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    
    fullname_csv = os.path.join(outdir, outname_csv)
    fullname_json = os.path.join(outdir, outname_json)
    
    # Flatten our scraped data
    flat = list(chain.from_iterable(data))
    players = list(map(flatten, flat))
    
    # Saving to csv
    df = pd.DataFrame(players)
    pipeline(df)
    df.to_csv(fullname_csv, index=False, encoding='utf-8-sig')
    
    # Saving to json and upload to dynamo db
    # Change table name
    tb_name = "FIFA22"
    with open(fullname_json, 'w') as fj:
        json.dump(players, fj)
    save_db(fullname_json, tb_name)


