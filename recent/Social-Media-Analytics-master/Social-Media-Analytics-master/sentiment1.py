import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
import json

with open("data\\yellow.txt",encoding="ascii") as f:
    for each_tweet in f:
        data = {}
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(each_tweet)
        data['Sentiment'] = sentiment
        data['text']=each_tweet


        json_data = json.dumps(data)
        print(json_data)
with open('yellow_off.json' ,'a') as d:

        d.write(json.dumps(json_data)+ '\n')
        d.close()

