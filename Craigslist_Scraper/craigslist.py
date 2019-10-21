from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

base_url = "https://toronto.craigslist.org/search/sss?query=car&sort=rel"

page = requests.get(base_url)

if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')

all_cars = bs.find('div', class_='content').find('ul', class_='rows').find_all('li')

# print(all_cars)
#car = all_cars[0]
# print(car)

data = {
    'Title': [],
    'Price': [],
    'Date': []
}

for item in all_cars:

    title = item.find('p').find('a').text
    if title:
        data['Title'].append(title)
    else:
        data['Price'].append('none')
    # print(title)

    price = item.find('span').text
    if price:
        data['Price'].append(price)
    else:
        data['Price'].append('none')
    # print(price)

    date = item.find('time').text
    if date:
        data['Date'].append(date)
    else:
        data['Date'].append('none')

# print(data)

table = pd.DataFrame(data, columns=['Title', 'Price', 'Date'])
table.index = table.index + 1
print(table)
table.to_csv('craigslist.csv', sep=',', index=False, encoding='utf-8')
