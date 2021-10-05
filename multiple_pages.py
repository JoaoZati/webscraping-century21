import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='


def interation(item):
    for column in item.find_all('div', {'class': 'columnGroup'}):
        if 'Age' in column.text:
            text = column.find('span', {'class': 'featureName'}).text
            return text


def scrapy_all_into_list(all, list):
    for item in all:
        d = {'price': item.find('h4', {'class': 'propPrice'}).text.replace('\n', '').replace(' ', ''),
             'address': item.find_all('span', {'class': 'propAddressCollapse'})[1].text}

        try:
            text_bed = item.find_all('span', {'class': 'infoBed'})[0].find('b').text
            d['bed'] = text_bed
        except:
            d['bed'] = None

        d['ages'] = interation(item)

        list.append(d)


list_dataframe = []
for page in range(0, 30, 10):
    url = f'{base_url}{page}.html'
    print(url)
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, 'html.parser')
    all = soup.find_all('div', {'class': "propertyRow"})

    scrapy_all_into_list(all, list_dataframe)

df_scrapy = pd.DataFrame(list_dataframe)
df_scrapy.to_csv('output_multiple.csv')
