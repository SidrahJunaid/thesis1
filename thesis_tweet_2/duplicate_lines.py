import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')


lst = []
with open('data\\tweets_with_healthy_keywords2.json') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    print (content)


new_list = []
for item in content:
   if item not in new_list:
     new_list.append(item )
     new_list.append('\n')
     with open('data\\no_duplicate_healthy_tweets.json','a') as t:
         t.write("%s\n" % item)



