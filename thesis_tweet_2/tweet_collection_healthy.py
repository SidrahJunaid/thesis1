import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

analyzer = SentimentIntensityAnalyzer()

with open("newtweet.txt", "r") as f:
    for each_tweet in f:

        sentiment = analyzer.polarity_scores(each_tweet)
        if sentiment['compound']==0.0:
            print (each_tweet)
        #data = {}

        # data['Sentiment'] = sentiment
        # data['text']=each_tweet

        #
        # json_data = json.dumps(data)
        # print(json_data)

