import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pymongo

# Starting URL (seed URL)
seed_url = 'https://www.nike.com/es/'

# Function to fetch and parse a page
def fetch_and_parse(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"Failed to fetch and parse {url}: {e}")
        return None

# Function to extract product URLs from a page
def extract_product_urls(page):
    product_links = page.find_all('a', class_='product-card__link-overlay')
    return [urljoin(seed_url, link['href']) for link in product_links]

# Set to keep track of visited URLs
visited_urls = set()

# List to store all product URLs
all_product_urls = []

# Queue for URLs to visit (start with the seed URL)
url_queue = [seed_url]

# Maximum number of pages to crawl (adjust as needed)
max_pages_to_crawl = 1

# Perform web crawling
while url_queue and len(all_product_urls) < max_pages_to_crawl:
    current_url = url_queue.pop(0)

    if current_url not in visited_urls:
        print(f"Crawling: {current_url}")

        page = fetch_and_parse(current_url)

        if page:
            visited_urls.add(current_url)
            product_urls = extract_product_urls(page)
            all_product_urls.extend(product_urls)

            # Extract and enqueue links to other pages (if needed)
            other_links = page.find_all('a', href=True)
            for link in other_links:
                next_url = urljoin(current_url, link['href'])
                if next_url.startswith(seed_url) and next_url not in visited_urls and next_url not in url_queue:
                    url_queue.append(next_url)

# List to store information for all shoes
shoes_info = []

# Initialize a Selenium WebDriver with ChromeOptions for M1 Mac
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')  # Run in headless mode (no browser window)
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(options=chrome_options)


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["shoes"]
collection = db["wisam"]

# Send a GET request and extract information for each shoe
for url in all_product_urls:
    # Use Selenium to execute JavaScript and load dynamic content
    driver.get(url)

    # Wait for dynamic content to load
    driver.implicitly_wait(5)

    # Parse the HTML content
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extracting available sizes using the updated selector
    size_elements = soup.select('button[data-qa="size-dropdown-button"]')
    sizes = [size_element.get_text(strip=True) for size_element in size_elements]

    # Extracting model name, brand, and price
    model_name = soup.find('h1', {'data-test': 'product-title'}).get_text(strip=True) if soup.find('h1', {'data-test': 'product-title'}) else 'Model Name Not Found'
    brand = 'Nike'
    price_tag = soup.find('div', {'data-test': 'product-price'})
    price = price_tag.get_text(strip=True) if price_tag else 'Price Not Found'

    # Extracting color and model number
    color_description_element = soup.find('li', class_='description-preview__color-description')
    color_description = color_description_element.get_text(strip=True) if color_description_element else 'Color Not Found'
    model_number_element = soup.find('li', class_='description-preview__style-color')
    model_number = model_number_element.get_text(strip=True) if model_number_element else 'Model Number Not Found'

    # Create a dictionary for the current shoe
    current_shoe_info = {
        "model_name": model_name,
        "brand": brand,
        "available_sizes": sizes,
        "price": price,
        "color_description": color_description,
        "model_number": model_number,
    }

    # Add the current shoe's information to the list
    shoes_info.append(current_shoe_info)

    # Insert data into MongoDB collection
    collection.insert_one(current_shoe_info)

# Close the MongoDB connection
client.close()

# Quit the Selenium WebDriver
driver.quit()

print(f"Data for shoes saved to MongoDB collection '{db}' in database '{collection}'")
