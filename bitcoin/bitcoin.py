import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Wrong Input")

# print(sys.argv)
try:
    n = float(sys.argv[1])

except ValueError:
    sys.exit("Wrong Input")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Request Error")

o = response.json()
rate = o["bpi"]["USD"]["rate"].replace(',','')
rate = float(rate)
amount = rate * n
print(f"${amount:,.4f}")