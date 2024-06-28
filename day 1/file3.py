import requests
import re
import json

def scrape_product_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return
    
    # Check if page is available
    if response.status_code != 200:
        print("na")
        return
    
    # Extract JSON data embedded in the page
    page_content = response.text
    json_pattern = re.compile(r'window\.__PRELOADED_STATE__ = (.*?);</script>', re.DOTALL)
    json_data_match = json_pattern.search(page_content)
    
    if not json_data_match:
        print("na")
        return

    json_data = json.loads(json_data_match.group(1))

    # Initialize variables to handle missing elements
    regular_price = "not found"
    sale_price = "not found"
    availability = "not found"
    
    try:
        product = json_data['productDetails'][list(json_data['productDetails'].keys())[0]]
        
        # Extract regular price
        if 'currentPrice' in product:
            regular_price = product['currentPrice']
        else:
            regular_price = "not found"
        
        # Extract sale price
        if 'originalPrice' in product:
            sale_price = product['originalPrice']
        else:
            sale_price = "not found"
        
        # Extract availability
        availability = 'In stock' if product['availabilityStatus'] == 'IN_STOCK' else 'Out of stock'
        
    except KeyError:
        print("na")
        return
    
    print(f"Regular Price: {regular_price}")
    print(f"Sale Price: {sale_price}")
    print(f"Availability: {availability}")

# Example usage
scrape_product_info('https://www.samsclub.com/p/josh-cellars-cabernet-sauvignon-750-ml/prod12550288')
