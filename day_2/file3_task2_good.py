# import requests

# url = 'https://www.heb.com/graphql'
# response = requests.get(url)
# print(response.text)

# import requests
# from lxml import html

# def scrape_heb_product_data(url):
#     # Make a GET request to the URL
#     response = requests.get(url)
    
#     # Check if request was successful
#     if response.status_code == 200:
#         # Parse the HTML content
#         tree = html.fromstring(response.content)
        
#         # Extract product information using CSS selectors
#         try:
#             price = tree.cssselect('.sc-hLBbgP.bDSlqu')[0].text_content()
#         except IndexError:
#             price = None
        
#         try:
#             promotional_price = tree.cssselect('.sc-gmeYpB.fElEHd')[0].text_content()
#         except IndexError:
#             promotional_price = None
        
#         try:
#             availability = tree.cssselect('.sc-fOICqy.jyOxZh')[0].text_content()
#         except IndexError:
#             availability = None
        
#         # Print or return the extracted data
#         print(f"Regular Price: {price}")
#         print(f"Promotional Price: {promotional_price}")
#         print(f"Availability: {availability}")
#     else:
#         print(f"Failed to retrieve data. Status code: {response.status_code}")

# # URL to scrape
# url = 'https://www.heb.com/product-detail/cupcake-vineyards-prosecco-187-ml-bottles/2699015'

# # Call the function to scrape data
# scrape_heb_product_data(url)



import requests
import parsel

def scrape_heb_product_data(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        selector = parsel.Selector(response.text)
        
        price = selector.css('.sc-9ca2d8c2-0::text').get()
        promotional_price = selector.css('.sc-gmeYpB.fElEHd::text').get()
        availability = selector.css('.sc-fOICqy.jyOxZh::text').get()
        
        print(f"Regular Price: {price}")
        print(f"Promotional Price: {promotional_price}")
        print(f"Availability: {availability}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


url = 'https://www.heb.com/product-detail/cupcake-vineyards-prosecco-187-ml-bottles/2699015'


scrape_heb_product_data(url)
