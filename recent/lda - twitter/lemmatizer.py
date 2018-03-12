# from nltk.stem import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.stem import WordNetLemmatizer
#
# lemmatizer = WordNetLemmatizer()
# ps = PorterStemmer()
#
# new_text =open("text.txt")
# new_text=new_text.read()
# words = word_tokenize(new_text)
#
# for w in words:
#
#     a=lemmatizer.lemmatize(w)
#
#
# print a
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import nltk
from nltk.stem import PorterStemmer
nltk.download('stopwords')
nltk.download('wordnet')

stopwords = set(stopwords.words('english'))
punctuation = set(string.punctuation)
lemmatize = WordNetLemmatizer()
ps=PorterStemmer()

def cleaning(article):
    one = " ".join([i for i in article.lower().split() if i not in stopwords])
    two = "".join(i for i in one if i not in punctuation)
    three = " ".join(ps.stem(i) for i in two.split())

    four = " ".join(lemmatize.lemmatize(i) for i in two.split())
    return four

print(cleaning("my name is Sidrah loves loving to be with you."))