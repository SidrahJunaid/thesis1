import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("alabama_healthy1.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext.txt','a')
        appendFile.write(" "+r)
        appendFile.close()
import contractions as ct

def contract(data1):
	if data1 is not None:
		data1 = data1.split()
		data1= [ct.contractions_list[word] if word in ct.contractions_list else word for word in data1]
		data1 = " ".join(data1)
	return data1

