f1 = open("clean_training_data\\final.txt",'r')
writer = open("clean_training_data\\final1.txt", 'a')
tweet = set()
index = 25
for row in f1:
    if row[:index] not in tweet:
        writer.write(row)
        tweet.add( row[:index] )
f1.close()
writer.close()