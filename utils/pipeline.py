def pipeline(df):
    """
    Pipe and pre process scraped data
    :param df:
    :return: processed data frame
    """

    # Convert value to exact numbers of Euros
    #df['value'] = df['value'].apply(convert_into_val)
    #df['wage'] = df['wage'].apply(convert_into_val)


    # Drop duplicates
    df.drop_duplicates(inplace=True, ignore_index=True)

def convert_into_val(value):
    value = value.strip('€')
    if value[-1] == 'M':
        return float(value[:-1]) * 1e6
    elif value[-1] == 'K':
        return float(value[:-1]) * 1e3
    else:
        return float(value)
