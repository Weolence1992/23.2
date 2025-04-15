import requests

from bs4 import BeautifulSoup

import pandas as pd

# while True: Если использовать цикл, то выберет информацию со всех 996 страниц(решил оставить лишь 1 страницу)

url = f'https://parfums.ru/fragrance?sort=discount'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
products = soup.find_all('div', class_='col-6 col-sm-4 prod_item js-ajax-item')

Parfums = []

for n in products:
    Brand = n.find('span', class_='unit-brand').text.strip()
    Name = n.find('h3', class_='unit-name').text.strip()
    Price_old = n.find('span', class_='unit-price price-old').text.strip()
    Price_new = n.find('span', class_='unit-price price-new').text.strip()

    Parfums.append({'Наименование': f'{Brand}  {Name}', 'Старая цена': Price_old, 'Новая цена': Price_new})

for i in Parfums:
    print(i) # Сделал для себя, что бы просмотреть содержимое словаря

df = pd.DataFrame(Parfums)
print(df) # Для себя, что бы посмотреть как выглядит таблица)

df.to_excel('parfums praces.xlsx')
