import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import datetime


consumer_key = '5rkFkJDFPVBVDSvtNtoVpFpgq'
consumer_secret = 'VkK5YIETgPFNgKwt1tFHRSrztnNW00cbVaxCUAgMYqGrI5VHxa'
access_token = '4843507186-Kc982XGeypByuevVKdAhbMmEwnOmWWxgw247hUV'
access_secret = 'bKFAS5HDMzRMuckOnbMIjwjDxnKzUeivIz5VbENrs4soR'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

def date_range(start,end):
   current = start
   while (end - current).days >= 0:
      yield current
      current = current + datetime.timedelta(seconds=1)

class TweetListener(StreamListener):
    def on_status(self, status):
        #api = tweepy.API(auth_handler=auth)
        #status.created_at += timedelta(hours=900)

        startDate = datetime.datetime(2017, 10, 07 )
        stopDate = datetime.datetime(2017, 10, 11)
        for date in date_range(startDate,stopDate):
            status.created_at = date
            print ("tweet " + str(status.created_at) +"\n")
            print (status.text + "\n")
            # You can dump your tweets into Json File, or load it to your database

stream = Stream(auth, TweetListener(), secure=True,language=['en'] )
#t = u"pizza" # You can use different hashtags
stream.filter(track=['apple juice','apples','apricots','bananas','blueberries','cantaloupe','cherries','fruit cocktail','grape juice','grapefruit','grapefruit juice','grapes','honeydew','kiwi fruit'])