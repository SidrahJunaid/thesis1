from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import pandas as pd
import numpy as np
import scipy as sp
from time import time
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO,
                   filename='running.log',filemode='w')

data = pd.read_csv('food_emotion\\final.txt', error_bad_lines=False)



data_text = data[['Tweets']]

print(data_text.head(3))

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
from nltk.stem import *
from nltk.stem.porter import *

stoplist_tw=['today','shes','can','ipa','mean','yet','keep','since','state','soon','one','wait','without','with','take','least','god','nude',
             'away','see','run','top','literally','change','one','star','went','tho','finally','else','cat','im','first','might','one','time',
             'look','old','guy','tree','city','bring','half','republic','post','maybe','head','people','monster','pop','pay','school',
             'gotta','gonna','drive','believe','ever','even','every','dont','wanna','like','please','may',
             'us','say','play','game','didnt','yeah','around','stop','wish','mom','bitch','someone','break','remember','amp',
             'got','hey','hmm','hoo','hop','iep','let','ooo','par','hold','whole','ive','want','place','go','feel','bag','cause','end',
             'last','right','still','place','cant','try','much','put','sure','look','think','ask','actually','youre','ya','piece',
             'guy','show','miss','pretty','true','name','rt','question','trump','ready','call','get','try','look','never','side','b',
            'pdt','pln','pst','wha','yep','yer','aest','didn','nzdt','via','double','bro','bet','earn','sales','country','move','come','anyone',
            'one','com','new','make','top','need','open','job','though','check','line','different','hard',
            'good','wow','yes','say','yay','do','would','thanks','thank','going','app','kinda','fast','whats','boy','grab','open','man','thats','join',
            'new','use','should','could','really','see','nice','win','give','talk','aint','case','stick','include','k','company',
            'while','back','sex','porn','saw','size','meet','know','u','also','lot','drop','anything','learn','probably','sound','e','become','walk','throw',
             'girl','video','watch','w','forget','bad','come','bc','hear','picture','years','stand','talk','almost','girls','time','twitter','gt','face','always',
             'real','sign','sometimes','happen','exactly','lil','women','live','stay','take','real','theres','picture','almost','seem','ticket']

stopwords = set(stopwords.words('english')+stoplist_tw)
punctuation = set(string.punctuation)
lemmatize = WordNetLemmatizer()
stems=SnowballStemmer('english')
import nltk

def cleaning(article):
    one = " ".join([i for i in article.lower().split() if i not in stopwords])
    # four = " ".join([stems.stem(i) for i in one.split()])

    four=" ".join([i for i in one.split() if len(i) > 2])
    #five = " ".join([i for i,tag in nltk.pos_tag(four.split()) if tag.startswith('NN')])

    two = "".join(i for i in four if i not in punctuation)


    three = " ".join(lemmatize.lemmatize(i,'v') for i in two.split())
    return three

text = data_text.applymap(cleaning)['Tweets']
text_list = [i.split() for i in text]
print(len(text_list))

print (text_list[0])


# Importing Gensim
import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
dictionary = corpora.Dictionary(text_list)
dictionary.save('dictionary.dict')
print (dictionary)


# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in text_list]
corpora.MmCorpus.serialize('corpus.mm', doc_term_matrix)

print (len(doc_term_matrix))
print (doc_term_matrix[100])


start = time()
# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=10, id2word = dictionary, passes=50)
print ('used: {:.2f}s'.format(time()-start))

print(ldamodel.print_topics(num_topics=2, num_words=4))


for i in ldamodel.print_topics():
    for j in i: print(j)


ldamodel.save('topic.model')


from gensim.models import LdaModel
loading = LdaModel.load('topic.model')


print(loading.print_topics(num_topics=10, num_words=4))

# import pyLDAvis.gensim
# import gensim
#
#
# d = gensim.corpora.Dictionary.load('dictionary.dict')
# c = gensim.corpora.MmCorpus('corpus.mm')
# lda = gensim.models.LdaModel.load('topic.model')
#
# data = pyLDAvis.gensim.prepare(lda, c, d)
# pyLDAvis.display(data)
#
#
# pyLDAvis.save_html(data,'vis.html')