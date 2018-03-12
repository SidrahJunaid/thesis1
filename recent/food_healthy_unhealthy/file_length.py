# filenames = ['ex\\1', 'ex\\clean_emojis_healthy_tweets.txt']
# with open('ex\\final.txt', 'w') as outfile:
#     for fname in filenames:
#         with open(fname) as infile:
#             for line in infile:
#                 outfile.write(line)



num_lines = sum(1 for line in open('ex\\positive_food_sentiment.txt'))
print(num_lines)