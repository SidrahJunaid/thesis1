# import json
# def remove_duplicates(infile):
#   index=10
#   storehouse = set(index)
#   with open('duo1.txt', 'w+') as out:
#     for line in open(infile):
#          if line not in storehouse:
#              out.write(line)
#              storehouse.add(line)
#
#
# # remove_duplicates('duo.txt')
#
f1 = open("clean_training_data\\clean_tweets_food_USA.txt",'r')
writer = open("clean_training_data\\rem_dup_clean_tweets_food_USA.txt", 'a')
tweet = set()
index = 25
for row in f1:
    if row[:index] not in tweet:
        writer.write(row)
        tweet.add( row[:index] )
f1.close()
writer.close()