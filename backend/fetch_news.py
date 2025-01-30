import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('NEWSAPI_KEY')

#figure out which api to use

def fetch_news(query="Politics",key=api_key):
    url = 
