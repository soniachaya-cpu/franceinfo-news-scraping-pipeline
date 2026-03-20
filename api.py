from fastapi import FastAPI
import pandas as pd

app = FastAPI()

DATA_PATH = "data/clean/articles_clean.csv"

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/articles")
def get_articles():
    df = pd.read_csv(DATA_PATH)
    return df.head(20).to_dict(orient="records")

@app.get("/stats")
def get_stats():
    df = pd.read_csv(DATA_PATH)
    return {
        "total_articles": len(df),
        "columns": list(df.columns)
    }

@app.get("/keywords")
def get_keywords():
    df = pd.read_csv(DATA_PATH)
    if "title" not in df.columns:
        return {"error": "No title column"}

    words = " ".join(df["title"].astype(str)).split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return dict(sorted_words[:10])