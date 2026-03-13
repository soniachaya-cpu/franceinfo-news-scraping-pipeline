import os
import csv
import time
import logging
from bs4 import BeautifulSoup
from scraper.fetcher import fetch_page

BASE_URL = "https://www.franceinfo.fr/sante/environnement?page={}"

PAGES_TO_SCRAPE = 10
DELAY = 2

RAW_OUTPUT = "data/raw/articles_raw.csv"
CLEAN_OUTPUT = "data/clean/articles_clean.csv"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def extract_articles(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []

    links = soup.select("a")

    for link in links:
        title = link.get_text(strip=True)
        url = link.get("href")

        if not title:
            continue

        if not url:
            continue

        if "/sante/" not in url and "/environnement/" not in url:
            continue

        if url.startswith("/"):
            url = "https://www.franceinfo.fr" + url

        articles.append({
            "title": title,
            "url": url,
            "category": "environment"
        })

    return articles


def save_csv(path, rows, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def clean_articles(rows):
    seen = set()
    clean = []

    for r in rows:

        title = r["title"].strip()

        if len(title) < 15:
            continue

        if title in seen:
            continue

        seen.add(title)
        clean.append({
            "title": title,
            "url": r["url"],
            "category": r["category"]
        })

    return clean


def scrape_pages():

    all_articles = []

    for page in range(1, PAGES_TO_SCRAPE + 1):

        url = BASE_URL.format(page)

        logging.info(f"Scraping page {page}")

        html = fetch_page(url)

        if not html:
            logging.warning("Failed to fetch page")
            continue

        articles = extract_articles(html)

        logging.info(f"Found {len(articles)} articles")

        all_articles.extend(articles)

        time.sleep(DELAY)

    return all_articles


def main():

    logging.info("Starting scraping pipeline")

    raw_articles = scrape_pages()

    logging.info(f"Total raw articles: {len(raw_articles)}")

    save_csv(RAW_OUTPUT, raw_articles, ["title", "url", "category"])

    clean = clean_articles(raw_articles)

    logging.info(f"Total clean articles: {len(clean)}")

    save_csv(CLEAN_OUTPUT, clean, ["title", "url", "category"])

    logging.info("Pipeline finished")


if __name__ == "__main__":
    main()
