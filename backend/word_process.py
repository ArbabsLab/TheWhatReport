import os
from fetch_news import fetch_news_keyword, fetch_news_source
from nltk.tokenize import word_tokenize
import nltk

#fetch the news data
data = fetch_news_keyword()

#extrsct only the articles
data = data['articles']

#grab the titles and description from the articles
data_titles = []
data_desc = []
for article in data:
    data_titles.append(article['title'])
    data_desc.append(article['description'])



#tokenize the titles
data_titles_tokenized = []
for doc in data_titles:
    data_titles_tokenized.append(word_tokenize(doc))

#remove the stop words and punctuation
stop_words = []
f = open(os.path.join('backend', 'stopwords.txt'), 'r')
for line in f.readlines():
    stop_words.append(line.strip())

#remove numbers and lowercase the words
data_titles_processed = []
for sent in data_titles_tokenized:
    for word in sent:
        if word.isalnum() and word not in stop_words:
            data_titles_processed.append(word.lower())



def getProcessedTitles():
    return data_titles_processed






        






