import string
from fetch_news import fetch_news_keyword, fetch_news_source
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk



#fetch the news data
data = fetch_news_keyword()

#extrsct only the articles
data = data['articles']

#grab the titles from the articles
data_titles = []
for article in data:
    data_titles.append(article['title'])



#tokenize the titles
data_titles_tokenized = []
for doc in data_titles:
    data_titles_tokenized.append(word_tokenize(doc))

#remove the stop words
nltk.download('stopwords')
stop_words = stopwords.words('english')
data_titles_processed = []
for sent in data_titles_tokenized:
    for word in sent:
        if word not in stop_words:
            data_titles_processed.append(word)


print(data_titles_processed)
        






