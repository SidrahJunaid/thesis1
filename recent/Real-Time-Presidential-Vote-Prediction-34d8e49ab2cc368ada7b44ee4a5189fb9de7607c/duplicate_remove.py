f1 = open("files\\tweets_unhealthy.txt",'r')
writer = open("files\\1", 'a')
tweet = set()
index = 50
for row in f1:
    if row[:index] not in tweet:
        writer.write(row)
        tweet.add( row[:index] )
f1.close()
writer.close()