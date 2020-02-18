import requests

STOCK_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/stocks.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    if cap.endswith('M'):
        return float(cap.strip('$M'))
    if cap.endswith('B'):
        return float(cap.strip('$B')) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    global data
    summed_cap = 0
    for stock in data:
        if stock['industry'] == industry:
            summed_cap += _cap_str_to_mln_float(stock['cap'])
    return round(summed_cap, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    global data
    highest_cap = max(data, key=lambda stock: _cap_str_to_mln_float(stock['cap']))
    # Using sort(list) and take the first element might be faster than max() because it exploits
    # the underlying list. But the data might be altered with this.
    return highest_cap['symbol']


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    from collections import Counter
    global data
    industries = [stock['sector'] for stock in data]
    counted = Counter(industries)
    del counted['n/a']
    most_common = counted.most_common()
    return most_common[0][0], most_common[-1][0]
