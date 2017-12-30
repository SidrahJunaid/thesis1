# import json
# tweets = []
# for line in open('newtweet_healthy.json', 'r'):
#     tweets.append(json.loads(line))
#     print (tweets)
#!/usr/bin/env python3
import json

with open('data\\no_duplicate_healthy_tweets.json', encoding='ascii') as file:
    for line in file:
        text = json.loads(line)
        print(text['location'])
