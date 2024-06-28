import requests
import parsel
import time

def scrape_dynamic_website(url):
    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1'
    }

    # Make a GET request to the URL
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content
        selector = parsel.Selector(response.text)
        
        # List of common CSS selectors for price, promotional price, and availability
        price_selectors = [
            '.sc-9ca2d8c2-0::text',  # Specific example provided
            '[class*="price"]::text',
            '[id*="price"]::text',
            '.price::text',
            '.pricing::text'
        ]
        
        promotional_price_selectors = [
            '.sc-gmeYpB.fElEHd::text',  # Specific example provided
            '[class*="promo"]::text',
            '[id*="promo"]::text',
            '.promo::text',
            '.discount::text'
        ]
        
        availability_selectors = [
            '.sc-fOICqy.jyOxZh::text',  # Specific example provided
            '[class*="avail"]::text',
            '[id*="avail"]::text',
            '.availability::text',
            '.stock::text'
        ]
        
        # Helper function to extract data using a list of selectors
        def extract_data(selectors):
            for selector in selectors:
                data = selector.css(selector).get()
                if data:
                    return data.strip()
            return "Not available"
        
        # Extract product information using the common selectors
        price = extract_data(price_selectors)
        promotional_price = extract_data(promotional_price_selectors)
        availability = extract_data(availability_selectors)
        
        # Print or return the extracted data
        print(f"Regular Price: {price}")
        print(f"Promotional Price: {promotional_price}")
        print(f"Availability: {availability}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

# URL to scrape (can be changed to test different websites)
url = 'https://www.heb.com/product-detail/cupcake-vineyards-prosecco-187-ml-bottles/2699015'

# Call the function to scrape data
scrape_dynamic_website(url)
