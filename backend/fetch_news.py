import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('NEWSAPI_KEY')

def fetch_news_keyword(query="Politics",sort_by = "popularity",page_size = "100", key=api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy={sort_by}&pageSize={page_size}&apiKey={key}"
    
    req = requests.get(url)

    return req.json()

def fetch_news_source(source="us", key=api_key):
    url = f"https://newsapi.org/v2/top-headlines?country={source}&apiKey={key}"
    
    req = requests.get(url)

    return req.json()

