from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    models_of_year = (entry['automaker'] for entry in data if entry['year'] == year)
    return Counter(models_of_year).most_common(1)[0][0]


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return set(entry['model']
               for entry in data
               if entry['automaker'] == automaker
               if entry['year'] == year)


def test():
    # for i in range(10):
    #     print(data[i])
    # print(most_prolific_automaker(2002))
    print(get_models('Volkswagen', 2008))


if __name__ == '__main__':
    test()
