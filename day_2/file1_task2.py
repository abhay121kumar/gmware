import requests
import json

def scrape_heb_product_data(url):
   
    response = requests.get(url)
    
    if response.status_code == 200:
        # Find the JSON data embedded in the HTML response
        json_data_start = response.text.find('window.INITIAL_STATE = ') + len('window.INITIAL_STATE = ')
        json_data_end = response.text.find('};', json_data_start) + 1
        
        # Extract and parse the JSON data
        product_json_str = response.text[json_data_start:json_data_end]
        try:
            product_data = json.loads(product_json_str)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON data: {str(e)}")
            return
        
        # Extract required information
        product_info = product_data.get('ProductInfo')
        if product_info:
            regular_price = product_info.get('regular_price')
            availability = product_info.get('stock_info', {}).get('available')
            promotional_price = product_info.get('promo_price')

            # Print or return the extracted data
            print(f"Regular Price: {regular_price}")
            print(f"Availability: {availability}")
            print(f"Promotional Price: {promotional_price}")
        else:
            print("Product information not found.")
        
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# URL to scrape
url = 'https://www.heb.com/product-detail/la-marca-prosecco-sparkling-wine-1-single-serve/1794510'

# scrape_heb_product_data(url)

response = requests.get(url)
print(response.text)
# print(response.status_code)
# resp = response.json()
# print(resp)