from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.zillow.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract property details
properties = []
for listing in soup.find_all('div', class_='property-listing'):
    name = listing.find('h2').text
    price = listing.find('span', class_='price').text
    location = listing.find('span', class_='location').text
    properties.append([name, price, location])

df = pd.DataFrame(properties, columns=['Name', 'Price', 'Location'])