import requests

# Define the URL and the payload for the POST request
url = "https://www.samsclub.com/api/node/vivaldi/browse/v2/products"
payload = {
    "productIds": ["prod12550288"],
    "type": "LARGE",
    "clubId": 6610
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "www.samsclub.com",
    "Origin": "https://www.samsclub.com",
    "Referer": "https://www.samsclub.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Define cookies extracted from the browser session
cookies = {
    # Add cookies here. Example format:
    # "cookie_name": "cookie_value",
}

# Create a session to maintain cookies
session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookies)

# Make the POST request
response = session.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    product = data['products'][0]
    
    # Extract regular price, promotional price, and availability
    regular_price = product.get('itemPrice', {}).get('listPrice')
    promotional_price = product.get('itemPrice', {}).get('offerPrice')
    availability = product.get('availability', {}).get('status')

    # Print the extracted information
    print(f"Regular Price: {regular_price}")
    print(f"Promotional Price: {promotional_price}")
    print(f"Availability: {availability}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)
