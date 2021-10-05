import requests
from bs4 import BeautifulSoup

url = 'https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'
request = requests.get(url)
content = request.content

soup = BeautifulSoup(content, 'html.parser')

# Extract div elements

all = soup.find_all('div', {'class': "propertyRow"})

all_0 = all[0]
value = all_0.text.split('$')[1].split(',')[0]
cents = all_0.text.split('$')[1].split(',')[1][:2]

price_all_0 = float(f'{value}.{cents}')

text_price = all[0].find('h4', {'class': 'propPrice'}).text
text_only_price = text_price.replace('\n', '').replace(' ', '')
