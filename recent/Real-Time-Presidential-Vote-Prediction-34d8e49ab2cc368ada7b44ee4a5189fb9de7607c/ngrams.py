# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.util import ngrams
#
# file1=open("text.txt" ,'r')
# for words in file1:
#     words=words.strip("\n")
#     words=words.split(" ")
#     word=["_".join(w) for w in ngrams(words,2)]
#     print word

#
# from google_ngram_downloader import readline_google_store
# fname, url, records = next(readline_google_store(ngram_len=2))
# print fname
# print(next(records))


import nltk
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

# change this to read in your data
finder = BigramCollocationFinder.from_words(
   nltk.corpus.genesis.words('english-web.txt'))

# only bigrams that appear 3+ times
finder.apply_freq_filter(3)

# return the 10 n-grams with the highest PMI
finder.nbest(bigram_measures.pmi, 10)


