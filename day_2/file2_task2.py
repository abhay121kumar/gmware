import requests
from bs4 import BeautifulSoup

# # Define the URL
# url = "https://www.heb.com/product-detail/la-marca-prosecco-sparkling-wine-1-single-serve/1794510"

# # Send a GET request to the URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find the elements containing the desired data
#     # Note: The actual class names and structure may vary, so inspect the page to find the correct selectors

#     # Regular price
#     regular_price = soup.find('span', {'class': 'css-regular-price-class-name'})  # Replace with actual class name
#     if regular_price:
#         regular_price = regular_price.text.strip()
#     else:
#         regular_price = "Not found"

#     # Check availability
#     availability = soup.find('div', {'class': 'css-availability-class-name'})  # Replace with actual class name
#     if availability:
#         availability = availability.text.strip()
#     else:
#         availability = "Not found"

#     # Promotional price
#     promotional_price = soup.find('span', {'class': 'css-promotional-price-class-name'})  # Replace with actual class name
#     if promotional_price:
#         promotional_price = promotional_price.text.strip()
#     else:
#         promotional_price = "Not found"

#     # Print the results
#     print(f"Regular Price: {regular_price}")
#     print(f"Availability: {availability}")
#     print(f"Promotional Price: {promotional_price}")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")




# import requests
# from bs4 import BeautifulSoup

# # Define the URL
# url = "https://www.heb.com/product-detail/la-marca-prosecco-sparkling-wine-1-single-serve/1794510"

# # Define headers to mimic a browser request
# headers = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
# #     "Accept-Language": "en-US,en;q=0.9",
# #     "Accept-Encoding": "gzip, deflate, br",
# #     "Connection": "keep-alive",
# #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     "authority":"www.heb.com",
#     "method":"GET",
#     "path":"/product-detail/la-marca-prosecco-sparkling-wine-1-single-serve/1794510",
#     "scheme":"https",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding":"gzip, deflate, br, zstd",
#    " Accept-Language":"en-US,en;q=0.9",
#     "Cache-Control":"max-age=0",
#     "Cookie":"DYN_USER_ID=18698742455; DYN_USER_CONFIRM=f9f5e252922293d73af6cd0cd8905cd1; USER_SELECT_STORE=false; CURR_SESSION_STORE=92; sessionContext=curbside; JSESSIONID=EW_D5pwoGEopmL8j7xaZCh0D_vOrqmX9RlSISuek; sst=hs:sst:87DNRipJUtxBFjDNxS5vJ; sst.sig=b26BG014mOHWHosz_jomuQVlmBi5ioPFzEX1GY3fsLg; visid_incap_2302070=r2l93xzSSGO8HTbr09atLiFcfmYAAAAAQUIPAAAAAAAX3iIO6VbMcOjaYBAQCxHH; incap_ses_707_2302070=nau8QgziqWszgjav2sTPCSNcfmYAAAAA+Wq4zEzi2kmc9mvAMGtmHQ==; AMP_MKTG_760524e2ba=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE; reese84=3:TthpqRAiBdg9vEWD18tWJg==:j0a+awGXlJNshNNQ5Sk6tUtMpVIx1tkVdGXiJhHF8wElPcxWCfjGvKLVaM/wyRxUcLmtJrQlN6FCk/FAh6siSU5/SJhQIX1FMoDNwLs07pVeyDo03HABXuPqnPFWNJPSvFF/Yrtk0bnR35gnZ+IXR8uMBgwWS5WbKHaUB0t9SE86dkVVQrni0Gst5dmSoQlvQNY4vz1XG8ymigNb24MBtKD/avuy8nrzkd/feqrNCjFbqUInXC+qHvpFGMVNRzyISzr0r93iSr//JsF/kfZkRdX28rhjCo+vW7g3v6OGRXY07lH8irW81MOl1xhesE9RjiVL03q4EcuFJ/1zpvDA+94aL+ScKLWGIc9WYM/X1mJ1S/bIhIhxKAs9Kb7AKzetYVUItOLZOGKDrqMshQq72zuvodhBf9AsIBCg6rb66IiyffbC2xsSXKIpHi6pZaUaVbZFcST8TzTpLHFN7maWWg==:3/3U103uKhDodJIWNv3uUMaGk8hHHmUxIv2Usu9PD+s=; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.369252534.1719557156; _gcl_au=1.1.1409691852.1719557156; _ga=GA1.2.1152731559.1719557155; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+28+2024+12%3A20%3A23+GMT%2B0530+(India+Standard+Time)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=12260f13-2c10-48ea-902f-94833fec13f2&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.heb.com%2Fproduct-detail%2Fla-marca-collezione-prosecco-sparkling-wine%2F2222199&groups=C0004%3A1; _dc_gtm_UA-26725300-5=1; _ga_WKSH6HYPT4=GS1.1.1719557155.1.1.1719557570.0.0.0; AMP_760524e2ba=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJoLTBlY2JmM2MzLTBhYzItNGUzMy1iZmEyLWU5NTUyYmZhMTA3ZSUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTk1NTcxNTQ5NjAlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzE5NTU3NTcwOTY5JTJDJTIybGFzdEV2ZW50SWQlMjIlM0EyNiUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMCU3RA==; AWSALB=Y6Co06ldEfXvVjPfi47DnuP48LZiKdm+ruyCFuGNCsDZ3f3E/EkAX36kB01VVpFxnEsgA6iOC/yXvXmglJ1pumbI0lkQ+NSfF/cy/4Oq+yFWSMlCM64KbtPoZtqJ",
#     "Priority":"u=0, i",
#     "Referer":"https://www.google.com/",
#     # Sec-Ch-Ua:"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"
#     # Sec-Ch-Ua-Mobile:?0
#     # Sec-Ch-Ua-Platform:"Windows"
#     # Sec-Fetch-Dest:document
#     # Sec-Fetch-Mode:navigate
#     # Sec-Fetch-Site:same-origin
#     # Sec-Fetch-User:?1
#     "Upgrade-Insecure-Requests":"1",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
# }

# # Send a GET request to the URL with headers
# response = requests.get(url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find the elements containing the desired data
#     # Note: The actual class names and structure may vary, so inspect the page to find the correct selectors

#     # Regular price
#     regular_price = soup.find('span', {'class': 'css-regular-price-class-name'})  # Replace with actual class name
#     if regular_price:
#         regular_price = regular_price.text.strip()
#     else:
#         regular_price = "Not found"

#     # Check availability
#     availability = soup.find('div', {'class': 'css-availability-class-name'})  # Replace with actual class name
#     if availability:
#         availability = availability.text.strip()
#     else:
#         availability = "Not found"

#     # Promotional price
#     promotional_price = soup.find('span', {'class': 'css-promotional-price-class-name'})  # Replace with actual class name
#     if promotional_price:
#         promotional_price = promotional_price.text.strip()
#     else:
#         promotional_price = "Not found"

#     # Print the results
#     print(f"Regular Price: {regular_price}")
#     print(f"Availability: {availability}")
#     print(f"Promotional Price: {promotional_price}")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")






url = "https://www.heb.com/product-detail/la-marca-prosecco-sparkling-wine-1-single-serve/1794510"

headers = {
    "authority": "www.heb.com",
    "method": "GET",
    "path": "/product-detail/la-marca-prosecco-sparkling-wine-1-single-serve/1794510",
    "scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookie": "DYN_USER_ID=18698742455; DYN_USER_CONFIRM=f9f5e252922293d73af6cd0cd8905cd1; USER_SELECT_STORE=false; CURR_SESSION_STORE=92; sessionContext=curbside; JSESSIONID=EW_D5pwoGEopmL8j7xaZCh0D_vOrqmX9RlSISuek; sst=hs:sst:87DNRipJUtxBFjDNxS5vJ; sst.sig=b26BG014mOHWHosz_jomuQVlmBi5ioPFzEX1GY3fsLg; visid_incap_2302070=r2l93xzSSGO8HTbr09atLiFcfmYAAAAAQUIPAAAAAAAX3iIO6VbMcOjaYBAQCxHH; incap_ses_707_2302070=nau8QgziqWszgjav2sTPCSNcfmYAAAAA+Wq4zEzi2kmc9mvAMGtmHQ==; AMP_MKTG_760524e2ba=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE; reese84=3:TthpqRAiBdg9vEWD18tWJg==:j0a+awGXlJNshNNQ5Sk6tUtMpVIx1tkVdGXiJhHF8wElPcxWCfjGvKLVaM/wyRxUcLmtJrQlN6FCk/FAh6siSU5/SJhQIX1FMoDNwLs07pVeyDo03HABXuPqnPFWNJPSvFF/Yrtk0bnR35gnZ+IXR8uMBgwWS5WbKHaUB0t9SE86dkVVQrni0Gst5dmSoQlvQNY4vz1XG8ymigNb24MBtKD/avuy8nrzkd/feqrNCjFbqUInXC+qHvpFGMVNRzyISzr0r93iSr//JsF/kfZkRdX28rhjCo+vW7g3v6OGRXY07lH8irW81MOl1xhesE9RjiVL03q4EcuFJ/1zpvDA+94aL+ScKLWGIc9WYM/X1mJ1S/bIhIhxKAs9Kb7AKzetYVUItOLZOGKDrqMshQq72zuvodhBf9AsIBCg6rb66IiyffbC2xsSXKIpHi6pZaUaVbZFcST8TzTpLHFN7maWWg==:3/3U103uKhDodJIWNv3uUMaGk8hHHmUxIv2Usu9PD+s=; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.369252534.1719557156; _gcl_au=1.1.1409691852.1719557156; _ga=GA1.2.1152731559.1719557155; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+28+2024+12%3A20%3A23+GMT%2B0530+(India+Standard+Time)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=12260f13-2c10-48ea-902f-94833fec13f2&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.heb.com%2Fproduct-detail%2Fla-marca-collezione-prosecco-sparkling-wine%2F2222199&groups=C0004%3A1; _dc_gtm_UA-26725300-5=1; _ga_WKSH6HYPT4=GS1.1.1719557155.1.1.1719557570.0.0.0; AMP_760524e2ba=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJoLTBlY2JmM2MzLTBhYzItNGUzMy1iZmEyLWU5NTUyYmZhMTA3ZSUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTk1NTcxNTQ5NjAlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzE5NTU3NTcwOTY5JTJDJTIybGFzdEV2ZW50SWQlMjIlM0EyNiUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMCU3RA==; AWSALB=Y6Co06ldEfXvVjPfi47DnuP48LZiKdm+ruyCFuGNCsDZ3f3E/EkAX36kB01VVpFxnEsgA6iOC/yXvXmglJ1pumbI0lkQ+NSfF/cy/4Oq+yFWSMlCM64KbtPoZtqJ",
    "Priority": "u=0, i",
    "Referer": "https://www.google.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}


response = requests.get(url, headers=headers)
print(response.text)
print()

# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')

#     # Find the elements containing the desired data
#     # Note: The actual class names and structure may vary, so inspect the page to find the correct selectors

#     # Regular price
#     regular_price = soup.find('span', {'class': 'css-regular-price-class-name'})  # Replace with actual class name
#     if regular_price:
#         regular_price = regular_price.text.strip()
#     else:
#         regular_price = "Not found"

#     # Check availability
#     availability = soup.find('div', {'class': 'css-availability-class-name'})  # Replace with actual class name
#     if availability:
#         availability = availability.text.strip()
#     else:
#         availability = "Not found"

#     # Promotional price
#     promotional_price = soup.find('span', {'class': 'css-promotional-price-class-name'})  # Replace with actual class name
#     if promotional_price:
#         promotional_price = promotional_price.text.strip()
#     else:
#         promotional_price = "Not found"

#     # Print the results
#     print(f"Regular Price: {regular_price}")
#     print(f"Availability: {availability}")
#     print(f"Promotional Price: {promotional_price}")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")










# url = "https://www.samsclub.com/api/node/vivaldi/browse/v2/products"
# product_IDs = ["prod21251710","prod25800239","prod21251673","prod12550288","prod1340737"]
# Store_IDs = [4735,6610,6613,6614,6616] 
# for product_id in product_IDs:
#     for store_id in Store_IDs:
#         headers = {
#             "authority": "www.heb.com",
#             "method": "GET",
#             "path": "/product-detail/la-marca-prosecco-sparkling-wine-1-single-serve/1794510",
#             "scheme": "https",
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#             "Accept-Encoding": "gzip, deflate, br, zstd",
#             "Accept-Language": "en-US,en;q=0.9",
#             "Cache-Control": "max-age=0",
#             "Cookie": "DYN_USER_ID=18698742455; DYN_USER_CONFIRM=f9f5e252922293d73af6cd0cd8905cd1; USER_SELECT_STORE=false; CURR_SESSION_STORE=92; sessionContext=curbside; JSESSIONID=EW_D5pwoGEopmL8j7xaZCh0D_vOrqmX9RlSISuek; sst=hs:sst:87DNRipJUtxBFjDNxS5vJ; sst.sig=b26BG014mOHWHosz_jomuQVlmBi5ioPFzEX1GY3fsLg; visid_incap_2302070=r2l93xzSSGO8HTbr09atLiFcfmYAAAAAQUIPAAAAAAAX3iIO6VbMcOjaYBAQCxHH; incap_ses_707_2302070=nau8QgziqWszgjav2sTPCSNcfmYAAAAA+Wq4zEzi2kmc9mvAMGtmHQ==; AMP_MKTG_760524e2ba=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE; reese84=3:TthpqRAiBdg9vEWD18tWJg==:j0a+awGXlJNshNNQ5Sk6tUtMpVIx1tkVdGXiJhHF8wElPcxWCfjGvKLVaM/wyRxUcLmtJrQlN6FCk/FAh6siSU5/SJhQIX1FMoDNwLs07pVeyDo03HABXuPqnPFWNJPSvFF/Yrtk0bnR35gnZ+IXR8uMBgwWS5WbKHaUB0t9SE86dkVVQrni0Gst5dmSoQlvQNY4vz1XG8ymigNb24MBtKD/avuy8nrzkd/feqrNCjFbqUInXC+qHvpFGMVNRzyISzr0r93iSr//JsF/kfZkRdX28rhjCo+vW7g3v6OGRXY07lH8irW81MOl1xhesE9RjiVL03q4EcuFJ/1zpvDA+94aL+ScKLWGIc9WYM/X1mJ1S/bIhIhxKAs9Kb7AKzetYVUItOLZOGKDrqMshQq72zuvodhBf9AsIBCg6rb66IiyffbC2xsSXKIpHi6pZaUaVbZFcST8TzTpLHFN7maWWg==:3/3U103uKhDodJIWNv3uUMaGk8hHHmUxIv2Usu9PD+s=; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.369252534.1719557156; _gcl_au=1.1.1409691852.1719557156; _ga=GA1.2.1152731559.1719557155; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+28+2024+12%3A20%3A23+GMT%2B0530+(India+Standard+Time)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=12260f13-2c10-48ea-902f-94833fec13f2&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.heb.com%2Fproduct-detail%2Fla-marca-collezione-prosecco-sparkling-wine%2F2222199&groups=C0004%3A1; _dc_gtm_UA-26725300-5=1; _ga_WKSH6HYPT4=GS1.1.1719557155.1.1.1719557570.0.0.0; AMP_760524e2ba=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJoLTBlY2JmM2MzLTBhYzItNGUzMy1iZmEyLWU5NTUyYmZhMTA3ZSUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTk1NTcxNTQ5NjAlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSUyQyUyMmxhc3RFdmVudFRpbWUlMjIlM0ExNzE5NTU3NTcwOTY5JTJDJTIybGFzdEV2ZW50SWQlMjIlM0EyNiUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMCU3RA==; AWSALB=Y6Co06ldEfXvVjPfi47DnuP48LZiKdm+ruyCFuGNCsDZ3f3E/EkAX36kB01VVpFxnEsgA6iOC/yXvXmglJ1pumbI0lkQ+NSfF/cy/4Oq+yFWSMlCM64KbtPoZtqJ",
#             "Priority": "u=0, i",
#             "Referer": "https://www.google.com/",
#             "Upgrade-Insecure-Requests": "1",
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
#         }


#         response = requests.request("GET", url, headers=headers)

#         # print(response.text)
#         resp = response.json()
#         print(resp)
#         try:
#             product = resp['payload']['products'][0]
            
#             # Regular price
#             regular_price = product['skus'][0]['clubOffer']['price']['finalPrice']['amount']
            
#             # Availability
#             availability = product['skus'][0]['clubOffer']['inventory']['status']
#             availability = 'In stock' if availability == 'AVAILABLE' else 'Out of stock'
            
#             # Promotion price (if available)
#             promotion_price = "not found"
#             promotions = product['promotions']
#             for promo in promotions:
#                 if 'finalPrice' in promo['price']:
#                     promotion_price = promo['price']['finalPrice']['amount']
#                     break
            
#             print(f"Regular Price: {regular_price}")
#             print(f"Availability: {availability}")
#             print(f"Promotional Price: {promotion_price}")
        
#         except (KeyError, IndexError) as e:
#             print(f"Error extracting data: {e}")

