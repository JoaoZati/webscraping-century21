import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'
request = requests.get(url)
content = request.content

soup = BeautifulSoup(content, 'html.parser')

# Extract price

all = soup.find_all('div', {'class': "propertyRow"})


def interation(item):
    for column in item.find_all('div', {'class': 'columnGroup'}):
        if 'Age' in column.text:
            text = column.find('span', {'class': 'featureName'}).text
            return text

    return None


list_dataframe = []
for item in all:
    d = {'price': item.find('h4', {'class': 'propPrice'}).text.replace('\n', '').replace(' ', ''),
         'address': item.find_all('span', {'class': 'propAddressCollapse'})[1].text}

    try:
        text_bed = item.find_all('span', {'class': 'infoBed'})[0].find('b').text
        d['bed'] = text_bed
    except:
        d['bed'] = None

    d['ages'] = interation(item)

    list_dataframe.append(d)


df_scrapy = pd.DataFrame(list_dataframe)
df_scrapy.to_csv('output_2.csv')
