import numpy as np
import pandas as pd
import time
import math
from nltk.corpus import stopwords

import numpy as np
import pandas as pd
import time
import math
from nltk.corpus import stopwords

from pyspark import SparkContext
from pyspark import Row
from pyspark.sql import SQLContext
from pyspark.ml.feature import Word2Vec
from pyspark.ml.clustering import KMeans

## Spark and sql contexts
sc = SparkContext('local', 'train-w2v') #change to cluster mode when needed
sqlContext = SQLContext(sc)

datapath = '/Users/sidra/PycharmProjects/py_project_make/alabama_healthy1.jso'
# Replace this line with:
# datapath = '/YOUR-PATH-TO-REPO/w2v/data/tweets.gz'

## Read Tweets
t0 = time.time()
tweets = sqlContext.read.json(datapath)
tweets.registerTempTable("tweets")
timeReadTweets = time.time() - t0

