from fetch_news import fetch_news_keyword, fetch_news_source
import nltk


data = fetch_news_keyword()

data = data['articles']

data_titles = []
for article in data:
    data_titles.append(article['title'])

print(data_titles)
