
# -*- coding: UTF-8 -*-
import re


def cleaningText(text):
        # The following regex just strips of an URL (not just http), any punctuations,
        # User Names or Any non alphanumeric characters.
       # text=(text.decode('unicode_escape').encode('ascii', 'ignore'))
        text = text.lower()  # remove capitals
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '.', text)
        # Convert www.* or https?://* to URL
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '.', text)
        # Convert @username to AT_USER
        text = re.sub('@[^\s]+', 'user', text)
        #text=re.compile(u'[\u2019|\u2018]', ',', text)
        # Remove additional white spaces
        text = re.sub('[\s]+', ' ', text)
        # Replace #word with word
        text = re.sub(r'#([^\s]+)', r'\1', text)
        return (text)


with open("tweet_text_healthy.txt",encoding='utf-8') as t1:
#print(raw_rdd.collect())
    t=[]
    for lines in t1:
    #data = raw_rdd.map(lambda line:line.split("\n"))
           x= cleaningText(lines)

           t.append(x)

    for lines1 in t:
        y=open("clean_tweet_text_healthy.txt","a",encoding='utf-8')
        y.write(lines1 +'\n')