import requests
from bs4 import BeautifulSoup

url = 'https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'
request = requests.get(url)
content = request.content

soup = BeautifulSoup(content, 'html.parser')

# Extract price

all = soup.find_all('div', {'class': "propertyRow"})

all_0 = all[0]
value = all_0.text.split('$')[1].split(',')[0]
cents = all_0.text.split('$')[1].split(',')[1][:2]

price_all_0 = float(f'{value}.{cents}')

text_price = all[0].find('h4', {'class': 'propPrice'}).text
text_only_price = text_price.replace('\n', '').replace(' ', '')

# extract address

text_address = all[0].find_all('span', {'class': 'propAddressCollapse'})[1].text

#extract beds

text_beds = all[1].find_all('span', {'class': 'infoBed'})[0].find('b').text

# making lists

list_prices = [
    item.find('h4', {'class': 'propPrice'}).text.replace('\n', '').replace(' ', '')
    for item in all
]

list_address = [
    item.find_all('span', {'class': 'propAddressCollapse'})[1].text
    for item in all
]

list_beds = []
for item in all:
    try:
        text_bed = item.find_all('span', {'class': 'infoBed'})[0].find('b').text
        list_beds.append(text_bed)
    except:
        list_beds.append(None)
