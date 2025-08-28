import requests

symbol = input("Enter symbol")
api_url = f'https://api.api-ninjas.com/v1/stockprice?ticker={symbol}'.format(symbol)
response = requests.get(api_url, headers={'X-Api-Key': '5j++PenVdh93DsTiGw4guQ==FuVQ1wYBhgcXmVXg'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
