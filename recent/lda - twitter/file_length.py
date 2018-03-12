filenames = ['food_emotion\\healthy_food_negative_sentiment.txt', 'food_emotion\\healthy_food_positive_sentiment.txt','food_emotion\\mixed_food_negative_sentiment.txt','food_emotion\\mixed_food_positive_sentiment.txt','food_emotion\\unhealthy_food_negative_sentiment.txt','food_emotion\\unhealthy_food_positive_sentiment.txt']
with open('food_emotion\\final.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)



num_lines = sum(1 for line in open('food_emotion\\final.txt'))
print(num_lines)