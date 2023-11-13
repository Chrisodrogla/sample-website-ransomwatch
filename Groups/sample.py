import os
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json

# Function to renew the TOR IP address
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="YOUR_TOR_PASSWORD")
        controller.signal(Signal.NEWNYM)

# TOR proxy settings
tor_proxy = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050',
}

def crawl_with_tor(url, max_depth=2, current_depth=0, discovered=set()):
    if current_depth > max_depth:
        return discovered

    try:
        response = requests.get(url, proxies=tor_proxy)
        if response.status_code == 200:
            discovered.add(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            links = [urljoin(url, link.get('href')) for link in soup.find_all('a')]

            for link in links:
                if link not in discovered and is_internal_link(url, link):
                    discovered = crawl_with_tor(link, max_depth, current_depth + 1, discovered)

    except Exception as e:
        print(f"Error crawling {url}: {e}")

    return discovered

def is_internal_link(base_url, link):
    base_domain = urlparse(base_url).netloc
    link_domain = urlparse(link).netloc
    return base_domain == link_domain

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    starting_urls_data = load_json('Groups/Overall_data/data_post.json')
    crawled_data = []

    for entry in starting_urls_data:
        starting_url = entry["download_data"]
        title = entry["ransomware_name"]

        renew_tor_ip()  # Renew Tor IP before starting
        discovered_websites = crawl_with_tor(starting_url)

        # Filter out websites that are already in data_post.json's "download_data"
        discovered_websites = [site for site in discovered_websites if site != starting_url]

        crawled_entry = {"ransomware_site": starting_url, "ransomware_name": title}
        for i, website in enumerate(discovered_websites, start=1):
            crawled_entry[f"Discovered website {i}"] = website

        crawled_data.append(crawled_entry)

    # Save the crawled data to crawled.json
    save_json('Groups/Overall_data/crawled.json', crawled_data)

    print("Crawling and saving completed.")
