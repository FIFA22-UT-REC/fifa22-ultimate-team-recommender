# Helper for pipeline
def convert_currency(value):
    value = value.strip('€')
    if value[-1] == 'M':
        return float(value[:-1]) * 1e6
    elif value[-1] == 'K':
        return float(value[:-1]) * 1e3
    else:
        return float(value)