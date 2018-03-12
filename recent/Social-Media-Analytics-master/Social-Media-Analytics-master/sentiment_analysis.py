import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

analyzer = SentimentIntensityAnalyzer()

with open("dup_rem_healthy\\dup_rem_healthy\\texas_healthy.json",encoding="ascii") as f:
    for each_tweet in f:

        sentiment = analyzer.polarity_scores(each_tweet)
        if sentiment['compound']>0.0 or sentiment['compound']==0.0:
           print (each_tweet)
           # print(sentiment['compound'])
           y = open("www\\vaderresults\\texas_healthy_vader_pos.txt", 'a')
           y.write(each_tweet)
        elif sentiment["compound"]< 0.0:
            print (each_tweet)
            y = open("www\\vaderresults\\texas_ healthy_vader_neg.txt", 'a')
            y.write(each_tweet)
            # y = open("sentiment_dataset_unhealthy_keyword\\SanDiego_negative_unhealthy.txt", 'a')
            # y.write(each_tweet)





