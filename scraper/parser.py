from bs4 import BeautifulSoup

def parse_articles(html, rubrique, sous_rubrique):

    soup = BeautifulSoup(html, "lxml")

    articles_data = []

    articles = soup.find_all("article")

    for art in articles:

        try:
            title = art.find("h2").get_text(strip=True)
        except:
            title = None

        try:
            url = art.find("a")["href"]
        except:
            url = None

        try:
            summary = art.find("p").get_text(strip=True)
        except:
            summary = None

        try:
            date = art.find("time").get_text(strip=True)
        except:
            date = None

        articles_data.append({
            "title": title,
            "date": date,
            "rubrique": rubrique,
            "sous_rubrique": sous_rubrique,
            "summary": summary,
            "url": url
        })

    return articles_data
