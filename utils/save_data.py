import os
import json
from utils.pipeline import pipeline
from utils.save_db import save_db


def save_data(data):
    """
    Save the data scraped to a .csv file
    :param data:
    :return: csv
    """

    # Define variables and directories to store data
    outname = "player_raw_data"
    outdir = "./data/raw"
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullname_csv = os.path.join(outdir, outname + ".csv")
    fullname_json = os.path.join(outdir, outname + ".json")

    # converts raw data scraped to processed df
    # through series of transformations
    df = pipeline(data)

    df.to_csv(fullname_csv, index=False, encoding='utf-8-sig')

    # Saving to json and upload to dynamo db
    # Change table name
    tb_name = "FIFA22"
    json_dict = df.to_dict("records")
    with open(fullname_json, 'w') as fj:
        json.dump(json_dict, fj)

    save_db(json_dict, tb_name)


