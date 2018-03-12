from collections import Counter
import nltk

def word_count(fname):
        list = ['broccoli', 'spinach', 'pizza', 'celery']
        for word in list:
          with open(fname) as f:
                f=f.split("\n")
                if word in f:
                    return Counter(f.read().split()).most_common(3)

print("Number of words in the file :",word_count("duo.txt"))