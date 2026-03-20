# FranceInfo News Scraping Pipeline + API

This project implements a structured web scraping pipeline that collects
environmental health news articles from Franceinfo.

The scraper automatically gathers article metadata including:
- title
- publication date
- category
- summary
- article URL

The pipeline is organized into modular components:

scraper/
fetcher.py      → downloads pages
parser.py       → extracts article data
cleaner.py      → cleans and normalizes dataset
config.py       → configuration parameters

Output dataset:
data/raw/articles_raw.csv
data/clean/articles_clean.csv

Technologies:
Python
BeautifulSoup
Requests
Pandas


## New Feature: API Layer

This project now includes a FastAPI-based API to expose processed data as JSON.

It allows:

- Accessing cleaned articles via `/articles`
- Getting dataset statistics via `/stats`
- Extracting keywords via `/keywords`

This transforms the pipeline into a usable data service.
