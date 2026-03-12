import pandas as pd
import logging

from scraper.fetcher import fetch_page
from scraper.parser import parse_articles
from scraper.cleaner import clean_dataset
from scraper.config import *

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def build_page_url(page):

    if page == 1:
        return BASE_URL

    return f"{BASE_URL}?page={page}"

def run_scraper():

    all_articles = []

    for page in range(1, MAX_PAGES + 1):

        url = build_page_url(page)

        logging.info(f"Scraping page {page}")

        html = fetch_page(url)

        if html is None:
            continue

        articles = parse_articles(html, RUBRIQUE, SUB_RUBRIQUE)

        all_articles.extend(articles)

    df = pd.DataFrame(all_articles)

    df.to_csv(RAW_DATA_PATH, index=False)

    df_clean = clean_dataset(df)

    df_clean.to_csv(CLEAN_DATA_PATH, index=False)

    logging.info("Scraping finished")

if __name__ == "__main__":
    run_scraper()
