#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#Variables that contains the user credentials to access Twitter API
access_token = "4843507186-Kc982XGeypByuevVKdAhbMmEwnOmWWxgw247hUV"
access_token_secret = "bKFAS5HDMzRMuckOnbMIjwjDxnKzUeivIz5VbENrs4soR"
consumer_key = "5rkFkJDFPVBVDSvtNtoVpFpgq"
consumer_secret =  "VkK5YIETgPFNgKwt1tFHRSrztnNW00cbVaxCUAgMYqGrI5VHxa"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        json_load = json.loads(data)
        print (data)
        # tweet = data.split(',"text":"')[1].split('","source')[0]
        texts = json_load['text']
        coded = texts.encode('utf-8')
        a=json_load['user']['location']
        #coded_loc = a.encode('utf-8')

        s = str(coded)
        #d=str(coded_loc)
        #print(s[2:-1])
        print(coded)
        loc = str(a)
        print (loc)
        saveFile = open('newtweet_healthy_2.json','a')

        data1 = {}
        t=data1['location'] =loc
        b=data1['text'] = s

        json_data1 = json.dumps(data1)
        print(json_data1)
        saveFile.write(json_data1)


        saveFile.write('\n')
        saveFile.close()
        return True


    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['apple juice','apples','apricots','bananas','blueberries','cantaloupe','cherries','fruit cocktail','grape juice','grapefruit','grapefruit juice','grapes','honeydew','kiwi fruit','lemons','limes','mangoes','nectarines','orange juice','oranges','papaya','peaches','pears','plums','prunes','raisins','raspberries','strawberries','tangerines','watermelon','acorn squash','artichokes','asparagus','avocado','bean sprouts','beets','black beans','bok choy','broccoli','brussels sprouts','butternut squash','cabbage','cassava','cauliflower','celery','collard greens','cowpeas','cucumbers','dark green leafy lettuce','eggplant','field peas','zucchini','white beans','watercress','water chestnuts','turnips','turnip greens','tomato juice','taro','sweet potatoes','split peas','spinach','soy beans','romaine lettuce','red peppers','plantains','pinto beans','okra','navy beans','mustard greens','mushrooms','mesclun','lentils','kidney beans','hubbard squash'],locations=[-74,40,-73,41],languages=['en'])