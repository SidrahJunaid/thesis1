f1 = open("clean_disease.txt",'r')
writer = open("dup_clean_disease.txt", 'a')
tweet = set()
index = 25
for row in f1:
    if row[:index] not in tweet:
        writer.write(row)
        tweet.add( row[:index] )
f1.close()
writer.close()