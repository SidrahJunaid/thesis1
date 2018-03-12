
from sklearn.feature_extraction.text import CountVectorizer
# # # list of text documents
# text =open("dup_tweets_healthy.txt",encoding="utf-8")
# vec=["tofu","Cucumbers"]
# #
# #
# # # create the transform
# vectorizer = CountVectorizer()
# # # tokenize and build vocab
# vectorizer.fit(vec)
# # # summarize
# print(vectorizer.vocabulary_)
# # # encode document
# vector = vectorizer.transform(text)
# # # summarize encoded vector
#
# print(vector.shape)
# print(type(vector))
# print(vector.toarray())
#print(vectorizer.get_feature_names())
#
# tags = ["cucumber","tofu","rice"]
#
# #
# # list_of_new_documents = [
# #   ["python, chicken"],
# #   ["linux, cow, ubuntu"],
# #   ["machine learning, bird, fish, pig"]
# #
# # ]
#
from sklearn.feature_extraction.text import CountVectorizer
# vect = CountVectorizer()
# tags = vect.fit_transform(tags)
#
# # vocabulary learned by CountVectorizer (vect)
# print(vect.vocabulary_)
#
#
# # counts for tags
# tags.toarray()

from gensim import corpora, models, matutils
from sklearn.cluster import KMeans
# documents = ProcDoc.read_doc()
documents =open("dup_tweets_healthy.txt",encoding="utf-8")
list=["tofu","cucumber"]
# remove common words and tokenize
texts = [[word for word in document.lower().split()] for document in documents]

texts = [[token for token in text] for text in texts]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

print ("TFIDF:")
corpus_tfidf = matutils.corpus2csc(corpus_tfidf).transpose()
print (corpus_tfidf)

