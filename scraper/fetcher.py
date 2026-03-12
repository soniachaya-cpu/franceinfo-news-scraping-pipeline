import requests
import time
import logging
from .config import DELAY

headers = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_page(url):

    try:
        response = requests.get(url, headers=headers)

        response.raise_for_status()

        time.sleep(DELAY)

        return response.text

    except Exception as e:

        logging.error(f"Error fetching {url}: {e}")

        return None
