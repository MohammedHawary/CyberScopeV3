from urllib.parse import urlparse, urlunparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import sys
import os
import re
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import DB_V3
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def check_internet(url='http://www.google.com', timeout=15, retries=3, delay=10):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            return True
        except (requests.ConnectionError, requests.Timeout):
            print(f"Attempt {attempt + 1} failed. Retrying in {delay} seconds...")
            time.sleep(delay)
    return False

def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def extract_links(url, base_url):
    try:
        response = requests.get(url, timeout=15)
        response.encoding = response.apparent_encoding  
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()
        for a_tag in soup.find_all("a", href=True):
            href = a_tag.get("href")
            full_url = urljoin(base_url, href)
            if is_valid(full_url) and full_url.startswith(base_url):
                links.add(full_url)
        return links
    except Exception as e:
        errorMessage = "Error in extract_links function " + str(e)
        print(errorMessage)
        return set()


def crawl(url, base_url, DELAY):
    if url in visited_urls:
        return
    visited_urls.add(url)
    links = extract_links(url, base_url)
    for link in links:
        if link not in visited_urls:
            time.sleep(DELAY)
            crawl(link, base_url, DELAY)


def remove_duplicates(input_list):
    seen = set()
    output_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    return output_list


def normalize_url(url):
    parsed_url = urlparse(url)
    normalized_path = parsed_url.path.rstrip('/')
    normalized_url = urlunparse(parsed_url._replace(path=normalized_path))
    return normalized_url

def remove_duplicates(input_list):
    seen = set()
    output_list = []
    for item in input_list:
        normalized_item = normalize_url(item)
        if normalized_item not in seen:
            seen.add(normalized_item)
            output_list.append(item)
    return output_list


def convert_to_url(input_string):
    ip_regex = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    domain_regex = re.compile(r'^(?!\-)([A-Za-z0-9-]{1,63})(\.[A-Za-z]{2,6})+$')
    url_regex = re.compile(r'^(https?://)?([A-Za-z0-9-]{1,63}\.)+[A-Za-z]{2,6}(/.*)?$')
    
    if url_regex.match(input_string):
        return input_string if input_string.startswith(('http://', 'https://')) else 'http://' + input_string
    
    elif ip_regex.match(input_string):
        return 'http://' + input_string
    
    elif domain_regex.match(input_string):
        return 'http://' + input_string
    
    else:
        raise ValueError("erro in convert_to_url Invalid input: not an IP address, domain name, or valid URL")


def save_urls(scan_name, target_url, Speed=0):
    if check_internet():
        scan_id = DB_V3.get_scan_id_by_name(scan_name)
        if scan_id:
            try:
                global visited_urls
                visited_urls = set()
                target_url = convert_to_url(target_url)
                base_url = "{0.scheme}://{0.netloc}".format(urlparse(target_url))

                crawl(target_url, base_url, Speed)
                for url in remove_duplicates(visited_urls):
                    DB_V3.insert_url(scan_id, url)
                errorMessage = 'Urls Extracted and Saved Successfully'
                print(errorMessage)
                return True, errorMessage
            except Exception as e:
                errorMessage = 'error in save_urls function ' + str(e)
                print(errorMessage)
                return False, errorMessage
        else:
            print('error in save_urls funcction the Scan Name Uncorrect')
    else:
        errorMessage = 'No Internet Connection!!'
        return False, errorMessage


def save_forms(scan_name, DELAY=0):
    scan_id = DB_V3.get_scan_id_by_name(scan_name)
    if scan_id:
        try:
            urls = DB_V3.get_urls_by_scan_id(scan_id)
            for url in urls:
                url_id = DB_V3.get_url_id_by_url(url)

                session = requests.Session()
                retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
                session.mount('http://', HTTPAdapter(max_retries=retries))

                response = requests.get(url, timeout=15)
                time.sleep(DELAY)

                if response.status_code == 200:

                    response.encoding = response.apparent_encoding

                    soup = BeautifulSoup(response.content, 'html.parser')
                    cleaned_list = soup.find_all('form')
                    forms = []
                    for form in cleaned_list:
                        form_html = str(form)
                        forms.append(form_html.strip().replace('\n', ''))

                    forms = json.dumps(forms)
                    DB_V3.insert_form(scan_id, url_id, forms)
                else:
                    print(f"error in save_forms Failed to fetch URL: {url}")
            errorMessage = 'Forms Extracted and Saved Successfully'
            print(errorMessage)
            return True, errorMessage
        except Exception as e:
            errorMessage = 'Error in save_forms function ' + str(e)
            print(errorMessage)
            return False, errorMessage
    else:
        errorMessage = 'Error in save_forms the scan name uncorrect or no urls data'
        print(errorMessage)
        return False, errorMessage


# save_forms("vulnweb")