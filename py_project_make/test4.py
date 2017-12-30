# import spark context
import string
import json
import re

# NLTK
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Spark ML
from pyspark.ml.feature import HashingTF, IDF, Word2Vec

# Spark MLlib
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import NaiveBayes,NaiveBayesModel
from pyspark.mllib.evaluation import MulticlassMetrics

# Spark Basic
from pyspark import SparkContext
from pyspark.sql import SQLContext,Row
from pyspark.sql.types import *
from pyspark.sql.functions import udf

##################
## Functions    ##
##################

# Module-level global variables for the `tokenize` function below
PUNCTUATION = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))
STEMMER = PorterStemmer()

twitter_raw = sc.textFile('tweetdata.json')

	# Parse JSON entries in dataset
	data = twitter_raw.map(lambda line: json.loads(line))

	# Take only english tweets
	data_english = data.filter(lambda line: line['lang']=='en')
	data_english.count()
##################
def tokenize(text):
    tokens = word_tokenize(text)
    lowercased = [t.lower() for t in tokens]
    no_punctuation = []
    for word in lowercased:
        punct_removed = ''.join([letter for letter in word if not letter in PUNCTUATION])
        no_punctuation.append(punct_removed)
    no_stopwords = [w.strip() for w in no_punctuation if not w in STOPWORDS]
    stemmed = [STEMMER.stem(w) for w in no_stopwords]
    return [w for w in stemmed]
    # return no_stopwords


# Cleaning the text field
##########################
def cleaningText(text):
    # The following regex just strips of an URL (not just http), any punctuations,
    # User Names or Any non alphanumeric characters.
    preprocesstext1 = ' '.join(
        re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(\d+)", " ", text).split()).strip().lower()

    # start replaceTwoOrMore
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    preprocesstext2 = pattern.sub(r"\1\1", preprocesstext1)
    return preprocesstext2


# Getting Polarity Score
##########################
def sentPolarityscore(text):
    ss = sid.polarity_scores(text)
    sent = ss['compound']
    return float(sent)


# Converting polarity into 1:Positive,0:Neutral and -1:Negative
###############################################################
def sentPolarity(text):
    ss = sid.polarity_scores(text)
    sent = ss['compound']
    if sent >= 0.0 and sent < 0.20:
        return 0
    elif sent >= 0.20 and sent <= 1.0:
        return 1
    else:
        return -1
    return sent