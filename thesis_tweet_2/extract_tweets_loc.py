import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


lst=[]
with open('location2.txt') as f:
    #for i in f.readlines():
       #lst.append(i.strip("\n))
       content=f.readlines()
       content=[x.strip() for x in content]
       # print (content)
      # print ("break")




with open('newtweet_healthy_1.json') as t:
     for line in t:
         text1 = json.loads(line)
         d=str(text1['location'])
         if d in content:
             #print "MATCH FOUND YAAAAAAYYYYYYYYYYY"
             print (line)
             save_File = open("data\\tweets_with_healthy_keywords2.json", 'a')
             save_File.write(line)
             save_File.close()

             # c=str(d)
         # print (d)
         # if any(word in c for word in content):
         #   print(text1[])





