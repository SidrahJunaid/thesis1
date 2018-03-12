import json
file=open("food_sentiment.txt", "a")
with open('dataset_tweets_healthy.json','r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = (tweet['text'])
        file.write(tokens)

