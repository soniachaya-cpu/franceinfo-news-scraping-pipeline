# franceinfo-news-scraping-pipeline

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
