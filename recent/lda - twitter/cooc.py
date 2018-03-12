Diseaselist = ["heart attack", "diabetes", "blood pressure", "heart disease", "breast cancer", "obesity", "overweight",
               " HIV ", "heartburn", "lung cancer"]
Foodlist = ["apple", "alfalfa", "arbys", "asparagus", "avocado", "bacon", "banana", "bbq", "beans", "beer", "beets",
            "blueberry", "bread", "broccoli", "cabbage", "cake", "cantaloupe", "carnitas", "carrot", "cauliflower",
            "celery", "cherry", "checkers", "chips", "chipotle", "chives", "coconut", "coffee", "cookie", "cranberry",
            "cucumber", "dates", "dessert", "donut", "egg", "elderberry", "figs", "garlic", "ginger", "gourd", "grape",
            "grapefruit", "greens", "grits", "guava", "habanero", "jambalaya", "ketchup", "kfc", "kiwi", "lemon",
            "lentils", "lettuce", "lime", "lobster", "maize", "mayo", "mango", "melon", "mint", "milkshake", "miso",
            "nuggets", "nutella", "olive", "onion", "orange", "pancake", "parsley", "peach", "peanut", "peas",
            "peppermint", "pepperoni", "peppers", "pickle", "pineapple", "pizza", "plum", "pomegranate", "potato",
            "pumpkin", "raisin", "rocket", " rum ", "salad", "salsa", "sausage", "salmon", "seaweed", "sesame", "soda",
            "soybean", "spinach", "squash", "strawberry", "sweetcorn", "tofu", "tomatillo", "tomato", "vegetable",
            "waffles", "wine", "zucchini"]

import glob

filepath = "food_emotion\healthy_food_negative_sentiment.txt"

cscore = []
for w1 in Foodlist:
    for w2 in Diseaselist:
        w2s = w2.replace(" ", "")
        score = 0
        confidencescore = 0
        for file in glob.glob(filepath):
            f = open(file, 'r').read()
            if w1 in f:
                if (w2 in f) or (w2s in f):
                    score = score + 1
                else:
                    pass
            else:
                pass
        confidencescore = str(score)
        coco = w1 + ", " + w2 + ", " + confidencescore
        cscore.append(coco)
print(cscore)

f = open('cooc_food.txt', 'w')
for item in cscore:
    f.write("%s\n" % item)
