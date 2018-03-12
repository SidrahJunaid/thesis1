import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

analyzer = SentimentIntensityAnalyzer()

with open("food_sentiment_ijcai\\positive_food_sentiment.txt",encoding="ascii") as f:
    for each_tweet in f:

        sentiment = analyzer.polarity_scores(each_tweet)
        if sentiment['compound']>0.0 or sentiment['compound']==0.0:
           print (each_tweet)
           # print(sentiment['compound'])
           y = open("food_emotion\\healthy_food_positive_sentiment.txt", 'a')
           y.write(each_tweet)
        elif sentiment["compound"]< 0.0:
            print (each_tweet)
            y = open("food_emotion\\healthy_food_negative_sentiment.txt", 'a')
            y.write(each_tweet)
            # y = open("sentiment_dataset_unhealthy_keyword\\SanDiego_negative_unhealthy.txt", 'a')
            # y.write(each_tweet)





