
def pipeline(df):
    """
    Pipe and pre process scraped data
    :param df:
    :return: processed data frame
    """

    # print(df.columns)
    # Convert height and weight to standard units
    # df['height'] = df['height'].apply(convert_into_cm)   # calls helper methods
    # df['weight'] = df['weight'].apply(lambda x: int(x[:-3])*0.45359237)

    # Convert value to exact numbers of Euros
    df['value'] = df['value'].apply(convert_into_val)
    df['wage'] = df['wage'].apply(convert_into_val)

    # adding the base url to player self link

    df['link'] = df['link'].apply(add_link)

    # Drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)


def add_link(link):
    base = "https://sofifa.com/"
    return base + format(link)


def convert_into_val(value):
    value = value.strip('€')
    if value[-1] == 'M':
        return float(value[:-1]) * 1e6
    elif value[-1] == 'K':
        return float(value[:-1]) * 1e3
    else:
        return float(value)


# def convert_into_cm(height):
#     height = height.strip('"')
#     foot, inches = height.split("'")
#     return int(foot) * 30.48 + int(inches) * 2.54
