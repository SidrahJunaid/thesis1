import json
import re
import sys
import os

import re
import unicodedata

def generateStopWordList():

    stopWords_dataset = "stopwords1.txt"

    stopWords = []

    try:
        fp = open(stopWords_dataset,'r')
        line = fp.readline()
        while line:
            word = line.strip()
            stopWords.append(word)
            line = fp.readline()
        fp.close()
    except:
        print("ERROR: Opening File")

    return stopWords


def preprocessing(dataSet):
    processed_data = []

    stopWords = generateStopWordList()

    for tweet in dataSet:

        temp_tweet = tweet
        tweet = re.sub('http\S+', " ", tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('@[^\s]+', '', tweet).lower()
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('[\s]+', ' ', tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)

        # tweet =re.sub('[\U0001F601-\U0001F636]', lambda y: unicodedata.name(y.group(0)), tweet)
        # tweet.replace(temp_tweet, tweet)

        tweet = re.sub('[0-9]+', "", tweet)
        tweet.replace(temp_tweet, tweet)

        for sw in stopWords:
            if sw in tweet:
                tweet = re.sub(r'\b' + sw + r'\b' + " ", "", tweet)

        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('[^a-zA-z ]', "", tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = re.sub('[\s]+', ' ', tweet)
        tweet.replace(temp_tweet, tweet)

        tweet = tweet.strip()

        processed_data.append(tweet)

    return processed_data
positive_data = open("clean_disease.txt").readlines()
positive_data = preprocessing(positive_data)
pw = open("clean_disease1.txt","w")

for i in positive_data:
    pw.write(str(i))
    pw.write("\n")
pw.close()