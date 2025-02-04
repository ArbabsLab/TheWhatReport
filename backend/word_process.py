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



#tokenize the titles and description
data_titles_tokenized = []
data_desc_tokenized = []
for doc in data_titles:
    data_titles_tokenized.append(word_tokenize(doc))

for desc in data_desc:
    data_desc_tokenized.append(word_tokenize(desc))


#remove the stop words and punctuation
stop_words = []
f = open(os.path.join('backend', 'stopwords.txt'), 'r')
for line in f.readlines():
    stop_words.append(line.strip())

#remove numbers and lowercase the words
data_titles_processed = []
data_desc_processed = []
for sent in data_titles_tokenized:
    for word in sent:
        if word.isalnum() and word not in stop_words:
            data_titles_processed.append(word.lower())


for s in data_desc_tokenized:
    new_s = ''
    for word in s:
        if word.isalnum() and word not in stop_words:
            new_s += word + ' '
    data_desc_processed.append(new_s)



def getProcessedTitles():
    return data_titles_processed

def getProcessedDesc():
    return data_desc_processed








        






