import requests
import json
from pprint import pprint

API_KEY = "demo"

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(parsed_response)


