# filenames = ['clean_emojis_healthy_tweets.txt', 'clean_emojis_unhealthy_tweets.txt']
# with open('final.txt', 'w') as outfile:
#     for fname in filenames:
#         with open(fname) as infile:
#             for line in infile:
#                 outfile.write(line)



num_lines = sum(1 for line in open('files\\1'))
print(num_lines)