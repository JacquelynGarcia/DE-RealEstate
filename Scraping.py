from bs4 import BeautifulSoup
import requests

# define the base URL
base_url = 'https://www.immoscout24.ch/en/house/buy/city-bern?r=7&map=1&pn='

# set the number of last page you retrieved previously
last_page = 2

# iterate through each page
for page_num in range(1, last_page + 1):
    url = f'{base_url}{page_num}'
    print(f"Scraping page {page_num} from URL: {url}")
    
    # fetch the page content
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        print(soup.prettify()[:1000]) 
        
        # find the relevant section for property listings
        listings = soup.find_all('article', class_='sc-1g3sn3w-0 dGsKFi')

        listings = soup.find_all('article', class_='sc-1g3sn3w-0 dGsKFi')
        print(f"Number of listings found on page {page_num}: {len(listings)}")
        
        # iterate through each listing and extract relevant information
        for listing in listings:
            # example of extracting information based on assumed structure
            title = listing.find('h2').text.strip() if listing.find('h2') else 'No title'
            price = listing.find('span', class_='sc-17h74je-0 bmyymz').text.strip() if listing.find('span', class_='sc-17h74je-0 bmyymz') else 'No price'
            location = listing.find('p', class_='sc-15yy2pl-0 cEhxSx').text.strip() if listing.find('p', class_='sc-15yy2pl-0 cEhxSx') else 'No location'
            description = listing.find('p', class_='sc-1g3sn3w-3 jPaFyj').text.strip() if listing.find('p', class_='sc-1g3sn3w-3 jPaFyj') else 'No description'
            
            # print extracted information
            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Location: {location}")
            print(f"Description: {description}")
            print("-" * 40)
    else:
        print(f"Failed to fetch data for page {page_num}. Status code: {response.status_code}")

