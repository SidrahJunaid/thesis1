from nltk.corpus import stopwords
import json
import re
from pyspark import SparkConf, SparkContext

conf=SparkConf().setMaster("local").setAppName("puSpark")

sc=SparkContext(conf=conf)
import contractions as ct

def contract(data1):
	if data1 is not None:
		data1 = data1.split()
		data1= [ct.contractions_list[word] if word in ct.contractions_list else word for word in data1]
		data1 = " ".join(data1)
	return data1

def cleaningText(text):
        # The following regex just strips of an URL (not just http), any punctuations,
        # User Names or Any non alphanumeric characters.
		text = text.lower()  # remove capitals
		text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
		# Convert www.* or https?://* to URL
		text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
		# Convert @username to AT_USER
		text = re.sub('@[^\s]+', 'AT_USER', text)
		# Remove additional white spaces
		text = re.sub('[\s]+', ' ', text)
		# Replace #word with word
		text = re.sub(r'#([^\s]+)', r'\1', text)

        # start replaceTwoOrMore
        # pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        # preprocesstext2 = pattern.sub(r"\1\1", preprocesstext1)
        return text
import spell as sp
def spell_check(data1):
	for s in data1:
		s = sp.correction(s)
	return data1
stops = set(stopwords.words("english"))
def remove_stop(data1):
	if data1 is not None:
		data1 = " ".join([w for w in data1.split() if w not in stops])
	return data1


raw_rdd = sc.textFile("unhealthy_train_pos.txt")
#print(raw_rdd.collect())
t=[]
for lines in raw_rdd.collect():
#data = raw_rdd.map(lambda line:line.split("\n"))
       x= contract(lines)
       y=spell_check(x)
       s=remove_stop(y)
       z=cleaningText(s)
       t.append(z)

for lines1 in t:
    y=open("abc.txt","a")
    y.writelines(lines1 + "\n")



