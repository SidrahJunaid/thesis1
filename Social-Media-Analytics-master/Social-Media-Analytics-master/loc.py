#Group-16
#Kartik
#Roma
#Vidyalakshmi

#Code by Prof.Gene Moo Lee, in section INSY-5378-001-2017-Spring

#!pip install Twython
from twython import TwythonStreamer
import sys
import json
import time

tweets = []

class MyStreamer(TwythonStreamer):
    '''our own subclass of TwythonStremer'''
  
    # overriding
    try:
        def on_success(self, data):
            if ('lang' in data and data['lang'] == 'en'):#('Trump' in data['lang'] or 'trump' in data['lang']):
                #put the name of the states under observation
                if ((data['user'])['location']) != None and ('New York City,NY' in ((data['user'])['location']) or 'NYC' in ((data['user'])['location'])  or 'New York City' in ((data['user'])['location']) or 'new york' in ((data['user'])['location'])  or 'NEWYORK' in ((data['user'])['location'])):
                    tweets.append(data)#.encode("utf-8")
                    print ('received tweet #', len(tweets), data['text'].encode("utf-8"))
                    print (data)
                    with open('data\\NewYorkCity_healthy_keywords.txt', 'a') as f:
                         f.write(json.dumps(data['text'].encode("utf-8")) + '\n')

                elif ((data['user'])['location']) != None and ('Los Angeles,CA' in ((data['user'])['location']) or 'Los Angeles' in ((data['user'])['location']) or 'LOS ANGELES,CA' in ((data['user'])['location']) or 'los angeles' in ((data['user'])['location']) or 'los Angeles,California' in ((data['user'])['location'])):
                    tweets.append(data)  # .encode("utf-8")
                    print( 'received tweet #', len(tweets), data['text'].encode("utf-8"))
                    print (data)
                    with open('data\\LosAngeles_TX_healthy_keywords.txt', 'a') as f:
                                 f.write(json.dumps(data['text'].encode("utf-8")) + '\n')

                          # json.dump(data['text'].encode("utf-8"),f,indent=2)
                                # f.write(data['text'])
                                # f.close()


                else:
                    print ('irrelevant')

            #
            # if len(tweets) >= 1000:
            #      self.store_json()
            #      self.disconnect()
            # # #if len(tweets)%5 == 0:
            # # #    time.sleep(10)
    except:
        pass

    # overriding
    try:
        def on_error(self, status_code, data):
            print (status_code, data)
            self.disconnect()
    except:
        pass
    #
    # def store_json(self):
    # #     #change the 'UT_AZ' value to the states under observation
    #     with open('healthyq.json', 'a') as f:
    #        json.dump(tweets['text'], f, indent=4)


if __name__ == '__main__':

 #   with open('sidrah.json', 'r') as f:
    #with open('../../../JG_Ch09_Getting_Data/04_api/gene_twitter_credentials.json', 'r') as f:
       # credentials = json.load(f)

    # create your own app to get consumer key and secret
    CONSUMER_KEY = '5rkFkJDFPVBVDSvtNtoVpFpgq'
    CONSUMER_SECRET = 'VkK5YIETgPFNgKwt1tFHRSrztnNW00cbVaxCUAgMYqGrI5VHxa'
    ACCESS_TOKEN = '4843507186-Kc982XGeypByuevVKdAhbMmEwnOmWWxgw247hUV'
    ACCESS_TOKEN_SECRET = 'bKFAS5HDMzRMuckOnbMIjwjDxnKzUeivIz5VbENrs4soR'

    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    #if len(sys.argv) > 1:
    #    keyword = sys.argv[1]
    #else:
    #    keyword = 'trump'
    
#To overcome ChunckedEncodingError-IncompleteRead
    counter=0
    while(len(tweets)<5):
        counter+=1
        try:
            if(counter%3!=0):
                #Taken from- https://dev.twitter.com/streaming/overview/request-parameters#track
                #Locations taken from http://boundingbox.klokantech.com/
                #change the location values & run again to get another state or combination of states.
                stream.statuses.filter(location='-74.2591,40.4774,-73.7003,40.9176,-118.6682,33.7037,-118.1553,34.3373',track=['apple juice','apples','apricots','bananas','blueberries','cantaloupe','cherries','fruit cocktail','grape juice','grapefruit','grapefruit juice','grapes','honeydew','kiwi fruit','lemons','limes','mangoes','nectarines','orange juice','oranges','papaya','peaches','pears','plums','prunes','raisins','raspberries','strawberries','tangerines','watermelon','acorn squash','artichokes','asparagus','avocado','bean sprouts','beets','black beans','bok choy','broccoli','brussels sprouts','butternut squash','cabbage','cassava','cauliflower','celery','collard greens','cowpeas','cucumbers','dark green leafy lettuce','eggplant','field peas','zucchini','white beans','watercress','water chestnuts','turnips','turnip greens','tomato juice','taro','sweet potatoes','split peas','spinach','soy beans','romaine lettuce','red peppers','plantains','pinto beans','okra','navy beans','mustard greens','mushrooms','mesclun','lentils','kidney beans','hubbard squash'],language=['en'],since = "2017-09-01", until = "2014-09-08",)
            else:
                #Taken from - http://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
                #to overcome error: 420 Easy there Turbo, too many requests recently 
                time.sleep(10)
        except:
            continue
