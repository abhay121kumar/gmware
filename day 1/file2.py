import requests
import json

url = "https://www.samsclub.com/api/node/vivaldi/browse/v2/products"
# ["prod21251710"], type: "LARGE", clubId: 4735
# productIds: ["prod25800239"], type: "LARGE", clubId: 6610
# productIds: ["prod21251673"], type: "LARGE", clubId: 6613
# "prod12550288 ,"clubId": 6614
# productIds: ["prod1340737"], type: "LARGE", clubId: 6616
# productIds: ["prod21251673"], type: "LARGE", clubId: 6616
product_IDs = ["prod21251710","prod25800239","prod21251673","prod12550288","prod1340737"]
Store_IDs = [4735,6610,6613,6614,6616]
# regular_price = 
# product_available = 
# promotion_price = 
for product_id in product_IDs:
    for store_id in Store_IDs:
        payload = json.dumps({
        "productIds": product_id,
        "type": "LARGE",
        "clubId": store_id
        })
        headers = {
        'Content-Type': 'application/json',
        'Cookie': 'SSLB=1; TS017260c8=0180a81bf3508f511b935f27ce178bd1324f3f0e76238c866c6936de58e11f3fccc2dcc0dba0b5e9a84322ef4f6bfb7e50567fc6e5; TS01b1959a=0180a81bf3508f511b935f27ce178bd1324f3f0e76238c866c6936de58e11f3fccc2dcc0dba0b5e9a84322ef4f6bfb7e50567fc6e5; ak_bmsc=BD9F4AEEC9184101CD9A14C9B264989B~000000000000000000000000000000~YAAQdgHARVEHclOQAQAAVlWUWBhFjrHH96dsZL4ZbLXzWX48AYw/wOu9w+BECqDR+2GJkQtMJmUSiPQu60m1/0ouHSJwhhpcv3qzEY5JjbSBsPtjGK+j+kcsHFk3sHJrqzTmb/XSP7s7c5Y/dS819I7oBHyPQztU1MvFMVak+0XnAHdzKT6o+WOh1mjfNrGY+K2ZjwIkOlovNliyk/i1K8E6CNQ6DGmeMFMS9wFM8LA86t4rXlKOAk287j4/10+F1yndDinoV+ljPWfDXXU33PQNQTXKhd3dNWE4hBKQxyuD1SoxB+7lFmt0EVaPZY1l1IUdx35JsOdQ3R84frAevTmUYWa5HHCZNq14/t2Z7BROxnmgLU0JT0/wEXtihjo=; az-reg=scus; bm_sv=86B096A84D7C8785231CBAA09CB15C95~YAAQdgHARcfIcVOQAQAAOEGSWBg8KG/Ty/CIdsL7AOj/GXsc3HN7LodFq1PcWrxyZzK8JvQNtlU8ejTV6kqtDjtfdbG9wYeCpv5fpT3QoAtaMWL056GChNFPEkmkg9GQGO3VJz62/xcluxH1DoXAw10a23q87fQR3RivGp/O9wYyHSiRtI1eeSZwyakDdVZacxBVuHQs/lEKFzMnJ/kNySO21I/LZx+iiXjxhSvz16IwtAvIzWT6QqZFDmOHBb//WDoU~1; bstc=emhtlZTI5jHceqVR-lw-5s; sams-pt=eyJ4NXQiOiJaRFJTMXNuUjlBTll1QkpaNmxybzF1Zmxmd3MiLCJraWQiOiI2NDM0NTJENkM5RDFGNDAzNThCODEyNTlFQTVBRThENkU3RTU3RjBCIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJleHQiOiI4SkZtWW1KbE1HRTBNREV4T0dFNVkyUm1ZbUptTURGaU0yTXpOakk0TnpFME56Qm1OalUxWVRZMVlXWTJOekprTlRBMlpqa3daamsyTnpBeU9XVTRPV0ZpT1RnME5XWmhPVFpqWVRFNFlqTmpNRFUzWmpkak5UTTVZVEZrTkRrd1kyWmpZVE14Wm1NNFlUSmlOREJsWldWa1l6UmxZVGM1WVRNNE4yWTVNalkyTW1NM01tWXlNV0V5TmpReFlXWm1PVEkyTURNelpqazFZams1WldKaU5UZ3oiLCJ2ZXIiOiIxLjAiLCJjaGkiOiJkZXNrdG9wIiwiZmJ0IjpmYWxzZSwiYWhiIjp7InYiOnRydWUsInAiOltdfSwib3ZyZCI6ZmFsc2UsInNoYSI6eyJ2Ijp0cnVlLCJwIjpbXX0sImV4cCI6MTcxOTQ3NjYzNCwiaWF0IjoxNzE5NDczMDM0LCJuYmYiOjE3MTk0NzMwMzQsImlzcyI6Imh0dHBzOi8vdGl0YW4uc2Ftc2NsdWIuY29tL2M4Y2MwNzBlLWRmZWQtNDVjOS1iZGE1LTI5ZDAwMTIxYWNiYi92Mi4wLyIsImp0aSI6IjFiZTcyMDVjLTM0OWUtNDE5NC1hOWQ3LTE5Y2UyMTQ2MTQ0OSJ9.WhfmBDHQqHrciohcNc07HIvTFwf0jlck7VrtaXYiNZKWEi4J5w7C8h8q7hSmE2RUqp88MkHiwmi5LrPSsCbUQuLWlZSWGDP89iWrQ2GK76LzOcPySEMzooS_FQUO-zpSEAOQUoBf-rX_ycdbLgJ1HUUbycjKbMgs3YCyrUfN84ZVOQx-oO6Rk_dW7DWYzRdr3hMjz9IdJ8HGrxebLjZtP2PVhWPR3XT4XIZHkoHIJbge_nYl0ssC2aF46qWb_N_KtbRRScossXElSZNYydSeZfoRemN9a8Sg8KbO-P6Jmd_iZAmLU6VlRjOSt4B7Be01YRzoVpQwN9docRCE39NpyGf1vFVA7m-5q1DlkvVLHiIn44l5_MEu0vh_-_NR5VESVenB10CBxB-42VDSIQOtH3lz17UmI-DAYLMeWHg82B80y04fQd1bI7hGyGTyb-3sxDGcfk0rU48r04j4TE2C8BUWsRg6kEcyGKXJHdjSl4F0VKlHrOchycM6QZ9ubrFnkK7pOwJ-b9XRSEwkPdMUtiPCBW1vgnkUk0zfCYlU-hZA-t-S1Wx2Lh2nb2yR9rW1WmCqjiapm9Txq-lnZdofp4QNibZVyhVmgaId1pG_PWTAir84HO7lqLNaqbSRV1BVT5u7sBhj-D2qhTuDg7QGl32uo7hywQz0BwWyaqwibBQ; seqnum=1; sxp-rl-SAT_ADD_ITEM-rn=78; sxp-rl-SCR_CLP_SWAP-rn=68; sxp-rl-SCR_SCRE-rn=99; sxp-rl-SCR_TII-rn=44; vtc=emhtlZTI5jHceqVR-lw-5s; xptwj=js:bb4a5d44ead38a32414a:vIAcJIT90sODkZ9evbghvNucYT2BsBE73pCGv0D2M/n7RGwO8T57p2SYa36RSPpS+4cnwphbmETv6s3vpeNFGiiK6qrCDJgFGZAuPrY1XHIfaIfl1MVCkZdmHTBQWg==; TS017c4a41=0180a81bf3508f511b935f27ce178bd1324f3f0e76238c866c6936de58e11f3fccc2dcc0dba0b5e9a84322ef4f6bfb7e50567fc6e5; akavpau_P1_Sitewide=1719473634~id=9239c7d54545d9756d2f44c7cda5e55e; sxp-rl-SAT_CME-rn=41; sxp-rl-SAT_DISABLE_SYN_PREQUALIFY-rn=1; sxp-rl-SAT_GEO_LOC-rn=70; sxp-rl-SAT_NEW_ORDERS_UI-rn=15; sxp-rl-SAT_ORDER_REPLACEMENT-rn=60; sxp-rl-SAT_REORDER_V4-rn=56; sxp-rl-SCR_CANCEL_ORDER_V3-rn=86; sxp-rl-SCR_CANRV4-rn=57; sxp-rl-SCR_NEXT3-rn=18; sxp-rl-SCR_OHLIMIT-rn=49; sxp-rl-SCR_SHAPEJS-rn=99; sxp-rl-SCR_VERIFICATION_V4-rn=92'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        # print(response.text)
        resp = response.json()
        print(resp)
        try:
            product = resp['payload']['products'][0]
            
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




# parsed_data = json.loads(data)

# # Extract necessary information
# product = parsed_data['payload']['products'][0]  # Access the first product in the list

# # Extract and print price, availability, and promotional price
# list_price = product['manufacturingInfo']['listPrice']['amount']
# sale_price = product['manufacturingInfo']['salePrice']['amount']
# availability = product['manufacturingInfo']['available']

# print(f"List Price: ${list_price}")
# print(f"Sale Price: ${sale_price}")
# print(f"Availability: {'In stock' if availability else 'Out of stock'}")
