import re
from collections import Counter
import nltk

list=['broccoli','spinach','pizza','celery']
for word in list:

    text1 =open('duo.txt').read().lower()
    for text1 in text1.split("\n"):
        text1=text1.split(' ')
        count = 0
        #while (count < len(list)):
        if word in text1:
              fdist1 = nltk.FreqDist(text1)
              list[word]=count+1
print (fdist1.most_common(2))
    # print Counter(words).most_common(3)



# text1 = 'hello he heloo hello hi '
# text1 = text1.split(' ')
# fdist1 = nltk.FreqDist(text1)
# print (fdist1.most_common(2))