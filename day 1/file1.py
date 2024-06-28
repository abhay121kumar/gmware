# import requests 
# from bs4 import BeautifulSoup
# response = requests.get('https://books.toscrape.com/')
# data = BeautifulSoup(response.text,'html.parser')
# data
# b1 = data.find(class_ = 'product_pod')
# b1
# base_url = 'https://books.toscrape.com/'
# b1_url = base_url + b1.h3.a['href']
# print(b1_url)
# title = data.h1.string
# title
# response = requests.get(b1_url)
# data = BeautifulSoup(response.text,'html.parser')
# data
# title = data.h1.string
# title
# price = data.find(class_ = 'price_color').string
# price
# qty = data.find(class_ = 'instock availability')
# qty
# qty = qty.contents[-1].strip()
# qty
# print(title)
# print(b1_url)
# print(price)
# print(qty)
# import re
# qty = int(re.search('\d+', qty).group())
# price = float(re.search('[\d.]+', price).group())
# print(title)
# print(b1_url)
# print(price)
# print(qty)
# book_details = []
# book_details.append([title, b1_url, price, qty])
# book_details.append([title, b1_url, price, qty])
# book_details
# import pandas as pd
# df = pd.DataFrame(book_details, columns = ['Title', 'Link', 'Price', 'Quantity In Stock'])
# df
# df.to_csv('books.csv')
# df.to_csv('books.csv', index = False)
# all_urls = ['https://books.toscrape.com/catalogue/page-1.html']
# cur_page = 'https://books.toscrape.com/catalogue/page-1.html'

# base_url = 'https://books.toscrape.com/catalogue/'

# response = requests.get(cur_page)

# while response.status_code == 200:
#     data = BeautifulSoup(response.text, 'html.parser')
#     next_page = data.find(class_ = 'next')
#     if next_page is None:
#         break
#     next_page_url = base_url + next_page.a['href']
#     print(next_page_url)
#     all_urls.append(next_page_url)
    
#     cur_page = next_page_url
#     response = requests.get(cur_page)
# response = requests.get('https://books.toscrape.com/')
# data = BeautifulSoup(response.text,'html.parser')
# b1 = data.find(class_ = 'product_pod')
# base_url = 'https://books.toscrape.com/'
# b1_url = base_url + b1.h3.a['href']
# print(b1_url)
# title = data.h1.string
# response = requests.get(b1_url)
# data = BeautifulSoup(response.text,'html.parser')
# title = data.h1.string
# price = data.find(class_ = 'price_color').string
# qty = data.find(class_ = 'instock availability')
# qty = qty.contents[-1].strip()
# import re
# qty = int(re.search('\d+', qty).group())
# price = float(re.search('[\d.]+', price).group())