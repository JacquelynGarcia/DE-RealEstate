from bs4 import BeautifulSoup
import requests

url = 'https://www.immoscout24.ch/en/house/buy/city-bern?r=7&map=1'

# make request and check if it succeeds
response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the data!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

# parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# find all anchor (<a>) elements and print their text and href
links = soup.findAll('a')
print(f"Number of links found: {len(links)}")

# print link content to inspect
for i, link in enumerate(links):
    print(f"Link {i}: Text: {link.text.strip()} - Href: {link.get('href')}")