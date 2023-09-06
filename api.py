import requests

response = requests.get('https://restcountries.com/v3.1/name/turkey')
data = response.json()

country_name = data[0]['name']['common']
print(f"Country Name: {country_name}")

