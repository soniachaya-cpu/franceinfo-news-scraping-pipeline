import pandas as pd

def clean_dataset(df):

    df = df.drop_duplicates()

    df["title"] = df["title"].str.strip()

    df["summary"] = df["summary"].fillna("")

    df["date"] = df["date"].fillna("unknown")

    return df
