import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('NEWSAPI_KEY')

def fetch_news(query="Politics",sort_by = "popularity",key=api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy={sort_by}&apiKey={key}"
    
    req = requests.get(url)

    return req.json
