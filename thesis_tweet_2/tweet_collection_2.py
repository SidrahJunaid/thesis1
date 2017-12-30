#import location as location
import tweepy
import json

ACCESS_TOKEN = '4843507186-Kc982XGeypByuevVKdAhbMmEwnOmWWxgw247hUV'
ACCESS_SECRET = 'bKFAS5HDMzRMuckOnbMIjwjDxnKzUeivIz5VbENrs4soR'
CONSUMER_KEY = '5rkFkJDFPVBVDSvtNtoVpFpgq'
CONSUMER_SECRET = 'VkK5YIETgPFNgKwt1tFHRSrztnNW00cbVaxCUAgMYqGrI5VHxa'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

latitude = 36.778261	# geographical centre of search
longitude = -119.417932	# geographical centre of search
max_range = 1 			# search range in kilometres
api = tweepy.API(auth)
api.wait_on_rate_limit = True
api.wait_on_rate_limit_notify = True

for tweet in tweepy.Cursor(api.search, q='',geocode = "%f,%f,%dkm" % (latitude, longitude, max_range) ,lang= 'en').items():
            print (tweet.created_at, tweet.text, tweet.user.id , tweet.user.followers_count,tweet.user.location)

            # with open('data.txt', 'w') as outfile:
            #     json.dump(tweet.created_at, tweet.text, tweet.user.id , tweet.user.followers_count,tweet.user.location.txt, outfile)