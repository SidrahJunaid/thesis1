# -*- coding: utf-8 -*-
text =open("food_emotion\\unhealthy_food_positive_sentiment.txt",'r')
text=text.read()
text=text.lower()

bigrams = ['blue cheese','cream cheese','cottage cheese','swiss cheese','miso cheese','cheddar cheese','cottage cheese','kiwi shake','']
for bigram in bigrams:
    text = text.replace(bigram, bigram.replace(" ",""))
    print (text)
    file=open ("unhealthy_food_positive_sentiment.txt","w")
    file.write(text)

