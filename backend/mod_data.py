from nltk.probability import FreqDist
from word_process import getProcessedTitles

TOP_COUNT = 20

freq_words = FreqDist(getProcessedTitles())
top_freq_words = freq_words.most_common(TOP_COUNT)



