import json
from textblob import TextBlob
import sys

#analyzer = SentimentIntensityAnalyzer()

with open("sentiment_textBlob\\unhealthy_tweets1.json",encoding="ascii") as f:
    for each_tweet in f:

        sentiment = TextBlob(each_tweet)
        # print (each_tweet,sentiment.polarity)
        if sentiment.polarity > 0.0 or sentiment.polarity == 0.0:
                    print(each_tweet)
                    # print(sentiment['compound'])
                    y = open("sentiment_textBlob\\unhealthy_train_pos.txt", 'a')
                    y.write(each_tweet)
        elif sentiment.polarity < 0.0:
                    print(each_tweet)
                    y = open("sentiment_textBlob\\unhealthy__train_neg.txt", 'a')
                    y.write(each_tweet)
