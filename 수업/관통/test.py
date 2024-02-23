import requests
from pprint import pprint as print

url = 'https://fakestoreapi.com/carts'

response = requests.get(url).json()

print(response)