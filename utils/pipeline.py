from flatten import flatten
from itertools import chain
import pandas as pd
from convert_dtype import convert_dtype
from convert_currency import convert_currency


def pipeline(data):
    """
    Pipe and pre process scraped data
    :param data:
    :return: processed data frame
    """
    data = list(map(flatten, chain.from_iterable(data)))
    df = pd.DataFrame(data)
    # drop duplicated data
    df.drop_duplicates(inplace=True, ignore_index=True)
    # convert all column names to lower case and 
    # replace space with underscore
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    # convert wage and value to float
    df["value"] = df["value"].apply(convert_currency)
    df["wage"] = df["wage"].apply(convert_currency)
    # convert all data to correct type
    df = convert_dtype(df)

    # mutate column to add more variable
    name_split = df["name"].str.split().str
    first_name = name_split[0]
    last_name = name_split[-1]
    df.insert(1, "first_name", first_name)
    df.insert(2, "last_name", last_name)
    return df
