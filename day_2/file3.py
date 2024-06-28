import requests
import json

url = "https://www.samsclub.com/api/node/vivaldi/browse/v2/products"

payload = json.dumps({
  "productIds": [
    "prod12550288"
  ],
  "type": "LARGE",
  "clubId": 661
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'SAT_ADD_ITEM=1; SCR_CLP_SWAP=0; SCR_SCRE=1; SCR_TII=1; SSLB=1; TS017260c8=01ae63dc70773eb2bc1e45f366255b7e9f3e523a6897b4a536a11b377cfc4443289b004edce3f5797af80cb0ef27cfea74fa3368f9; TS01b1959a=01ae63dc70773eb2bc1e45f366255b7e9f3e523a6897b4a536a11b377cfc4443289b004edce3f5797af80cb0ef27cfea74fa3368f9; ak_bmsc=78B71DD0FB0BE24C9A682F65A5041051~000000000000000000000000000000~YAAQdgHARVk4k1OQAQAA3AWfWRjETSdCoEIfmMciM6ERDAWAaWqHn7daK7npPMky+vbmoOjydWkFzB3rZzFJiHEm/cnAFZhsjSbYx0oovy4dKEFSgN7qENDkUVw+/C9m/WYB/mWDoxw2MRTt2iXoe6/ar/3B2fLIaycyDng85xjrD3PkTgJSMj0ucB6gX4xQ0Elwig7m9fP97AFzumIq5JDQWaadrT/YzhLtUsH7kLQLmZeltAnmAQ0N2d+2vfpdszsJcuAsIcl/4Ib2LO85cXzoDspC0XYWzcGGxJNSu+Lkr1Ni63SEwFyWCPl9NCeA98wRLU4EXJ+6H+L5TMryGYC2eDitp/6WHEXELJ74q1EnQT2ZVQnUXctPxOwW7f8=; az-reg=scus; bstc=TD9P-VPyMgvvoRP2eEsE5g; sams-pt=eyJ4NXQiOiJaRFJTMXNuUjlBTll1QkpaNmxybzF1Zmxmd3MiLCJraWQiOiI2NDM0NTJENkM5RDFGNDAzNThCODEyNTlFQTVBRThENkU3RTU3RjBCIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJleHQiOiI4SkZtWW1KbE1HRTBNREV4T0dFNVkyUm1ZbUptTURGaU0yTXpOakk0TnpFME56Qm1OalUxWVRZMVlXWTJOekprTlRBMlpqa3daamsyTnpBeU9XVTRPV0ZpT1RnME5XWmhPVFpqWVRFNFlqTmpNRFUzWmpkak5UTTVZVEZrTkRrd1kyWmpZVE14Wm1NNFlUSmlOREJsWldWa1l6UmxZVGM1WVRNNE4yWTVNalkyTW1NM01tWXlNV0V5TmpReFlXWm1PVEkyTURNelpqazFZams1WldKaU5UZ3oiLCJ2ZXIiOiIxLjAiLCJjaGkiOiJkZXNrdG9wIiwiZmJ0IjpmYWxzZSwiYWhiIjp7InYiOnRydWUsInAiOltdfSwib3ZyZCI6ZmFsc2UsInNoYSI6eyJ2Ijp0cnVlLCJwIjpbXX0sImV4cCI6MTcxOTQ5NDExMiwiaWF0IjoxNzE5NDkwNTEyLCJuYmYiOjE3MTk0OTA1MTIsImlzcyI6Imh0dHBzOi8vdGl0YW4uc2Ftc2NsdWIuY29tL2M4Y2MwNzBlLWRmZWQtNDVjOS1iZGE1LTI5ZDAwMTIxYWNiYi92Mi4wLyIsImp0aSI6IjYwZjNlOTZjLWE4YjYtNGI1Ni1hZTkzLTQwMThlZmFmMjc4NCJ9.sT4zTCey5vzL-NcTjrqKW5WbYcNZ7DnSKTKN23vYmFo9531PHgPnRTmSGsahTArOID_KcCq_55El_NM1RyL4kuWgb4t47OsVlu30yzkJHW-is_TNZb1Jcnq0jDf4xlt58scZa6XDowF9ftjsopmTMogJRcjQTp1Fa692Gg3Pq4ZnGSLrq8dx3COWFveYoBWCpNj0mzhAwxcW4eIFBjlPIEwqcpNk5BX_ifwW7b4R1cBN4KwvVcJYEJcDz7qCfl339ed9wZbMl6vXTZ9--ZMzemW_PDTzioP9j22afgvIyzIeTCm2z4cEyb0STS8YZJ4oPhhLdyGaVr9rJTx9Eyx8s2YvBqqKCKgCCsVHWda1dMKAtt1OuOVFBEBSpse1mjhtzPemUB_eIfDTxc1CffgJc155qw7-h2z5UV0A5veIMrnmwfksQEwnSmGBRXjk-guRCK7Hoh-X4zesvZGLxCWml77yee6rVcm4C-9OVWx8lqzS2iEE-cSuoSP2t-SeSpAbYThPetFLOYyF8s0Hp_BgCiVJZeoifilBflESRKOB8ifsMxi4y0lJkPhzz1cdVinyyTty0BvSPXlnc6QSJvwSzDKwyVUcTFoh9bh5myx_swC1XKCRcUv1MLMXnfHWR3aerNiBHj1i7kpcZaybZ8VLbjCQWVbIHmyJ_3FpLVvOBWU; seqnum=1; sxp-rl-SAT_ADD_ITEM-c=r|1|100; sxp-rl-SAT_ADD_ITEM-rn=78; sxp-rl-SCR_CLP_SWAP-c=r|1|50; sxp-rl-SCR_CLP_SWAP-rn=68; sxp-rl-SCR_SCRE-c=r|1|100; sxp-rl-SCR_SCRE-rn=99; sxp-rl-SCR_TII-c=r|1|100; sxp-rl-SCR_TII-rn=44; vtc=emhtlZTI5jHceqVR-lw-5s; xptwj=js:517ff735e3cb97ba534f:t/bKzMNTKOl7zNwBFzxIDo02pfONSwhPr1hLyzdK117Mlp7HcjH0fCDiqvGVlmIrX1tgAVwnmfBKrHXg6pBZ4JY6j5gcFJHng0RpasahiPW3G+Xtf5SJbvFX; SAT_CME=1; SAT_DISABLE_SYN_PREQUALIFY=0; SAT_GEO_LOC=0; SAT_NEW_ORDERS_UI=0; SAT_ORDER_REPLACEMENT=0; SAT_REORDER_V4=0; SCR_CANCEL_ORDER_V3=0; SCR_CANRV4=1; SCR_NEXT3=1; SCR_OHLIMIT=0; SCR_SHAPEJS=0; SCR_VERIFICATION_V4=0; TS017c4a41=01ae63dc70773eb2bc1e45f366255b7e9f3e523a6897b4a536a11b377cfc4443289b004edce3f5797af80cb0ef27cfea74fa3368f9; akavpau_P1_Sitewide=1719491112~id=b5e1c131cd95097410e356ca224ae6c6; sxp-rl-SAT_CME-c=r|1|100; sxp-rl-SAT_CME-rn=41; sxp-rl-SAT_DISABLE_SYN_PREQUALIFY-c=r|1|0; sxp-rl-SAT_DISABLE_SYN_PREQUALIFY-rn=1; sxp-rl-SAT_GEO_LOC-c=r|1|50; sxp-rl-SAT_GEO_LOC-rn=70; sxp-rl-SAT_NEW_ORDERS_UI-c=r|1|0; sxp-rl-SAT_NEW_ORDERS_UI-rn=15; sxp-rl-SAT_ORDER_REPLACEMENT-c=r|1|0; sxp-rl-SAT_ORDER_REPLACEMENT-rn=60; sxp-rl-SAT_REORDER_V4-c=r|1|0; sxp-rl-SAT_REORDER_V4-rn=56; sxp-rl-SCR_CANCEL_ORDER_V3-c=r|1|0; sxp-rl-SCR_CANCEL_ORDER_V3-rn=86; sxp-rl-SCR_CANRV4-c=r|1|100; sxp-rl-SCR_CANRV4-rn=57; sxp-rl-SCR_NEXT3-c=r|1|100; sxp-rl-SCR_NEXT3-rn=18; sxp-rl-SCR_OHLIMIT-c=r|1|0; sxp-rl-SCR_OHLIMIT-rn=49; sxp-rl-SCR_SHAPEJS-c=r|1|0; sxp-rl-SCR_SHAPEJS-rn=99; sxp-rl-SCR_VERIFICATION_V4-c=r|1|0; sxp-rl-SCR_VERIFICATION_V4-rn=92'
}

response = requests.request("POST", url=url, headers=headers, data=payload)

# print(response.text)
resp = response.json()
# print(resp)
print(response.status_code)

cookies = {
    # Add cookies here. Example format:
    "SAT_GS": "1",
    "SAT_JN_TY": "0",
    "SAT_CPUCP": "0",
    "SAT_CXO_SMS": "1",
    "SAT_SAF": "1",
    "SAT_POBOX": "1",
    "SCR_CSFLP": "1",
    "SAT_SPSH": "1",
    "SSLB": "1",
    "TS017260c8": "0126ea5edbef91053f88cdcc819e06b62b1cfcaae8867940bc954f9afa23449cde97250aa0004d48b00c58e5e2fa6e7206135f653a",
    "bstc": "X0yNq3XI-NBDs6BMmrPRYs",
    "vtc": "Ri2KzOPXsHJKzRjhq_Eyao",
    "TS017c4a41": "01dfbd54591d2237e94ab4ac866b60d09bd6b180f9f72779225db4ac84fe134ba42ed331e87fe54f247a219217fe9b8ff830a94796",
    "seqnum": "32",
    "sams-pt": "eyJ4NXQiOiJaRFJTMXNuUjlBTll1QkpaNmxybzF1Zmxmd3MiLCJraWQiOiI2NDM0NTJENkM5RDFGNDAzNThCODEyNTlFQTVBRThENkU3RTU3RjBCIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJleHQiOiI4SkZtWW1KbE1HRTBNREV4T0dFNVkyUm1ZbUptTURGaU0yTXpOakk0TnpFME56Qm1OalUxWVRZMVlXWTJOekprTlRBMlpqa3daamsyTnpBeU9XVTRPV0ZpT1RnME5XWmhPVFpqWVRFNFlqTmpNRFUzWmpkak5UTTVZVEZrTkRrd1kyWmpZVE14Wm1NNFlUSmlOREJsWldWa1l6UmxZVGM1WVRNNE4yWTVNalkyTW1NM01tWXlNV0V5TmpReFlXWm1PVEkyTURNelpqazFZams1WldKaU5UZ3oiLCJ2ZXIiOiIxLjAiLCJjaGkiOiJkZXNrdG9wIiwiZmJ0IjpmYWxzZSwiYWhiIjp7InYiOnRydWUsInAiOltdfSwib3ZyZCI6ZmFsc2UsInNoYSI6eyJ2Ijp0cnVlLCJwIjpbXX0sImV4cCI6MTcxOTU1NDMwMCwiaWF0IjoxNzE5NTUwNzAwLCJuYmYiOjE3MTk1NTA3MDAsImlzcyI6Imh0dHBzOi8vdGl0YW4uc2Ftc2NsdWIuY29tL2M4Y2MwNzBlLWRmZWQtNDVjOS1iZGE1LTI5ZDAwMTIxYWNiYi92Mi4wLyIsImp0aSI6ImU3NzU2ZTZkLThhNDctNGVjOC04MWViLTQzOTJiZTI0YjNlMCJ9.C_lD7KsYMnUXJc4PnIcpO3AjZsH6FtaCV8jtYjIhHInnwsG6SorMx-NSQTDYGh5XdAkNpuhpbRAbuYa7rPJmYrhMZI-vnuS8DQrP0Jm6uo0wDrY0X1sQn2bhkFP3hlmDF9nOfE0Mw8-d48RIhi8_CHzNbqzBv_4CxPoh1lfpN5VIRPy2yFA…",
    "xptwj": "js:5401a0999e66c1691a74:2oHzrkRvQE+lezsFffYaEMgXi+vuzwGBVaLl6+T7eW+VD48AUNoqAfKDOeoHqfOFX/exHK44InIecHOpIqtFMROBxokre02CiLm76qkA95MdntNrmS/uBw==",
    "TSbdf847b3027": "080d322835ab20001bec5810a74ff8e07c1dc9c102f40ec63798da728fe01e290970286d65c8421a08a87f5106113000a90b720251c763a3380e92612dda5fe8e318cb89c8be2389deef6575bbef539d447ecde44270fd98915d4867f0a1c4e5",
    "TS01b1959a": "01dfbd54591d2237e94ab4ac866b60d09bd6b180f9f72779225db4ac84fe134ba42ed331e87fe54f247a219217fe9b8ff830a94796",
    "akavpau_P1_Sitewide": "1719554118~id=33786399201b7a35513e790883f4b4c3"
}
