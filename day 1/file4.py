import requests
import json

# url = "https://www.samsclub.com/api/node/vivaldi/browse/v2/products"
# # productIds: ["prod21251673"], type: "LARGE", clubId: 6613
# payload = json.dumps({
# "productIds": ["prod12550288"],
# "type": "LARGE",
# "clubId": 6614
# })
# headers = {
# 'Content-Type': 'application/json',
# 'Cookie': 'SSLB=1; TS017260c8=0180a81bf3508f511b935f27ce178bd1324f3f0e76238c866c6936de58e11f3fccc2dcc0dba0b5e9a84322ef4f6bfb7e50567fc6e5; TS01b1959a=0180a81bf3508f511b935f27ce178bd1324f3f0e76238c866c6936de58e11f3fccc2dcc0dba0b5e9a84322ef4f6bfb7e50567fc6e5; ak_bmsc=BD9F4AEEC9184101CD9A14C9B264989B~000000000000000000000000000000~YAAQdgHARVEHclOQAQAAVlWUWBhFjrHH96dsZL4ZbLXzWX48AYw/wOu9w+BECqDR+2GJkQtMJmUSiPQu60m1/0ouHSJwhhpcv3qzEY5JjbSBsPtjGK+j+kcsHFk3sHJrqzTmb/XSP7s7c5Y/dS819I7oBHyPQztU1MvFMVak+0XnAHdzKT6o+WOh1mjfNrGY+K2ZjwIkOlovNliyk/i1K8E6CNQ6DGmeMFMS9wFM8LA86t4rXlKOAk287j4/10+F1yndDinoV+ljPWfDXXU33PQNQTXKhd3dNWE4hBKQxyuD1SoxB+7lFmt0EVaPZY1l1IUdx35JsOdQ3R84frAevTmUYWa5HHCZNq14/t2Z7BROxnmgLU0JT0/wEXtihjo=; az-reg=scus; bm_sv=86B096A84D7C8785231CBAA09CB15C95~YAAQdgHARcfIcVOQAQAAOEGSWBg8KG/Ty/CIdsL7AOj/GXsc3HN7LodFq1PcWrxyZzK8JvQNtlU8ejTV6kqtDjtfdbG9wYeCpv5fpT3QoAtaMWL056GChNFPEkmkg9GQGO3VJz62/xcluxH1DoXAw10a23q87fQR3RivGp/O9wYyHSiRtI1eeSZwyakDdVZacxBVuHQs/lEKFzMnJ/kNySO21I/LZx+iiXjxhSvz16IwtAvIzWT6QqZFDmOHBb//WDoU~1; bstc=emhtlZTI5jHceqVR-lw-5s; sams-pt=eyJ4NXQiOiJaRFJTMXNuUjlBTll1QkpaNmxybzF1Zmxmd3MiLCJraWQiOiI2NDM0NTJENkM5RDFGNDAzNThCODEyNTlFQTVBRThENkU3RTU3RjBCIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJleHQiOiI4SkZtWW1KbE1HRTBNREV4T0dFNVkyUm1ZbUptTURGaU0yTXpOakk0TnpFME56Qm1OalUxWVRZMVlXWTJOekprTlRBMlpqa3daamsyTnpBeU9XVTRPV0ZpT1RnME5XWmhPVFpqWVRFNFlqTmpNRFUzWmpkak5UTTVZVEZrTkRrd1kyWmpZVE14Wm1NNFlUSmlOREJsWldWa1l6UmxZVGM1WVRNNE4yWTVNalkyTW1NM01tWXlNV0V5TmpReFlXWm1PVEkyTURNelpqazFZams1WldKaU5UZ3oiLCJ2ZXIiOiIxLjAiLCJjaGkiOiJkZXNrdG9wIiwiZmJ0IjpmYWxzZSwiYWhiIjp7InYiOnRydWUsInAiOltdfSwib3ZyZCI6ZmFsc2UsInNoYSI6eyJ2Ijp0cnVlLCJwIjpbXX0sImV4cCI6MTcxOTQ3NjYzNCwiaWF0IjoxNzE5NDczMDM0LCJuYmYiOjE3MTk0NzMwMzQsImlzcyI6Imh0dHBzOi8vdGl0YW4uc2Ftc2NsdWIuY29tL2M4Y2MwNzBlLWRmZWQtNDVjOS1iZGE1LTI5ZDAwMTIxYWNiYi92Mi4wLyIsImp0aSI6IjFiZTcyMDVjLTM0OWUtNDE5NC1hOWQ3LTE5Y2UyMTQ2MTQ0OSJ9.WhfmBDHQqHrciohcNc07HIvTFwf0jlck7VrtaXYiNZKWEi4J5w7C8h8q7hSmE2RUqp88MkHiwmi5LrPSsCbUQuLWlZSWGDP89iWrQ2GK76LzOcPySEMzooS_FQUO-zpSEAOQUoBf-rX_ycdbLgJ1HUUbycjKbMgs3YCyrUfN84ZVOQx-oO6Rk_dW7DWYzRdr3hMjz9IdJ8HGrxebLjZtP2PVhWPR3XT4XIZHkoHIJbge_nYl0ssC2aF46qWb_N_KtbRRScossXElSZNYydSeZfoRemN9a8Sg8KbO-P6Jmd_iZAmLU6VlRjOSt4B7Be01YRzoVpQwN9docRCE39NpyGf1vFVA7m-5q1DlkvVLHiIn44l5_MEu0vh_-_NR5VESVenB10CBxB-42VDSIQOtH3lz17UmI-DAYLMeWHg82B80y04fQd1bI7hGyGTyb-3sxDGcfk0rU48r04j4TE2C8BUWsRg6kEcyGKXJHdjSl4F0VKlHrOchycM6QZ9ubrFnkK7pOwJ-b9XRSEwkPdMUtiPCBW1vgnkUk0zfCYlU-hZA-t-S1Wx2Lh2nb2yR9rW1WmCqjiapm9Txq-lnZdofp4QNibZVyhVmgaId1pG_PWTAir84HO7lqLNaqbSRV1BVT5u7sBhj-D2qhTuDg7QGl32uo7hywQz0BwWyaqwibBQ; seqnum=1; sxp-rl-SAT_ADD_ITEM-rn=78; sxp-rl-SCR_CLP_SWAP-rn=68; sxp-rl-SCR_SCRE-rn=99; sxp-rl-SCR_TII-rn=44; vtc=emhtlZTI5jHceqVR-lw-5s; xptwj=js:bb4a5d44ead38a32414a:vIAcJIT90sODkZ9evbghvNucYT2BsBE73pCGv0D2M/n7RGwO8T57p2SYa36RSPpS+4cnwphbmETv6s3vpeNFGiiK6qrCDJgFGZAuPrY1XHIfaIfl1MVCkZdmHTBQWg==; TS017c4a41=0180a81bf3508f511b935f27ce178bd1324f3f0e76238c866c6936de58e11f3fccc2dcc0dba0b5e9a84322ef4f6bfb7e50567fc6e5; akavpau_P1_Sitewide=1719473634~id=9239c7d54545d9756d2f44c7cda5e55e; sxp-rl-SAT_CME-rn=41; sxp-rl-SAT_DISABLE_SYN_PREQUALIFY-rn=1; sxp-rl-SAT_GEO_LOC-rn=70; sxp-rl-SAT_NEW_ORDERS_UI-rn=15; sxp-rl-SAT_ORDER_REPLACEMENT-rn=60; sxp-rl-SAT_REORDER_V4-rn=56; sxp-rl-SCR_CANCEL_ORDER_V3-rn=86; sxp-rl-SCR_CANRV4-rn=57; sxp-rl-SCR_NEXT3-rn=18; sxp-rl-SCR_OHLIMIT-rn=49; sxp-rl-SCR_SHAPEJS-rn=99; sxp-rl-SCR_VERIFICATION_V4-rn=92'
# }

# response = requests.request("POST", url=url, headers=headers, data=payload)
# resp = response.json()
# print(resp)


# Function to solve CAPTCHA using a hypothetical CAPTCHA solving service
def solve_captcha(captcha_challenge):
    # Replace with actual CAPTCHA solving service API endpoint and key
    api_key = 'your_api_key'
    api_url = f'https://api.captchaservice.com/solve'
    
    payload = {
        'api_key': api_key,
        'captcha_challenge': captcha_challenge
    }

    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            result = response.json()
            if result['success']:
                return result['solution']
            else:
                print(f"CAPTCHA solving failed: {result.get('error', 'Unknown error')}")
        else:
            print(f"Failed to connect to CAPTCHA solving service: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error during CAPTCHA solving request: {e}")
    
    return None


captcha_challenge = "Enter the CAPTCHA challenge text here"
captcha_solution = solve_captcha(captcha_challenge)

if captcha_solution:
    print(f"Solved CAPTCHA: {captcha_solution}")
    # Now continue with your script, using the solved CAPTCHA as needed
else:
    print("CAPTCHA solving failed or service unavailable")


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
    
    try:
        json_data = response.json()
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return
    
    # Extracting data from JSON
    try:
        product = json_data['payload']['products'][0]
        
        # Regular price
        regular_price = product['skus'][0]['clubOffer']['price']['finalPrice']['amount']
        
        # Availability
        availability = product['skus'][0]['clubOffer']['inventory']['status']
        availability = 'In stock' if availability == 'AVAILABLE' else 'Out of stock'
        
        # Promotion price (if available)
        promotion_price = "not found"
        promotions = product['promotions']
        for promo in promotions:
            if 'finalPrice' in promo['price']:
                promotion_price = promo['price']['finalPrice']['amount']
                break
        
        print(f"Regular Price: {regular_price}")
        print(f"Availability: {availability}")
        print(f"Promotional Price: {promotion_price}")
        
    except (KeyError, IndexError) as e:
        print(f"Error extracting data: {e}")
        return

# Example usage
scrape_product_info('https://www.samsclub.com/p/josh-cellars-cabernet-sauvignon-750-ml/prod12550288')


