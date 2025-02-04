from nltk.probability import FreqDist
from word_process import getProcessedTitles, getProcessedDesc
from sklearn.feature_extraction.text import TfidfVectorizer

TOP_COUNT = 20

freq_words = FreqDist(getProcessedTitles())
top_freq_words = freq_words.most_common(TOP_COUNT)

corpus = getProcessedDesc()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

feature_names = vectorizer.get_feature_names_out()
tfidf_scores = X.toarray()

top_features = []
for i, doc in enumerate(corpus):
    scores = list(zip(feature_names, tfidf_scores[i]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
    top_features.append([word for word,score in sorted_scores])

def getTopWords():
    return top_features


    



