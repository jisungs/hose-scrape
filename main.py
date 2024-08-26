import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.trulia.com/NY/New_York/"
END_URL = "https://www.trulia.com/NY/New_York/25_p/"

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}

res = requests.get(URL, headers=header)

soup = BeautifulSoup(res.text, 'lxml')


li_elms = soup.select('#main-content>div.gljvbF>div.jVJhkn>div.gkLIqp>ul>li')

asstes = []

for li in li_elms:
    price_tag = li.find('div', {'data-testid': 'property-price'})
    if price_tag:
        price = price_tag.get_text(strip=True)
    else:
        price = 'N/A'

    if price != 'N/A':
        asstes.append({
            'Price':price
        })
        print(price)

with open('NY_assets.csv', 'w', newline='', encoding='utf-8') as f:
    filenames = ['Price']
    writer = csv.DictWriter(f, fieldnames=filenames)

    writer.writeheader()
    for item in asstes:
        writer.writerow(item)
print('부동산 가격이 저장되었습니다.')