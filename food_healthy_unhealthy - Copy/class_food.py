import fileinput
from collections import defaultdict

class food_classify(object):
    def food_senti(self):


        with open("foodlist1_lexicon.txt", encoding='utf-8') as f:
            fields = {}
            for line in f:
                x = line.split(",")
                s = x[0]
                b = x[1]
                fields[s] = b.strip("\n")

        print(fields)

        text = "clean_training_data\\rem_dup_clean_tweets_food_USA.txt"
        #fields = {'carrots': '1', 'celery': '1', 'peas': '1', 'spinach': '1', 'cauliflower': '1', 'broccoli': '1', 'cabbage': '1', 'tomato': '1', 'eggplant': '1', 'oranges': '1', 'apples': '1', 'bananas': '1', 'pineapple': '1', 'pear': '1', 'plum': '1', 'apricot': '1', 'grapefruit': '1', 'peach': '1', 'cherry': '1', 'scalloped potatoes': '1', 'baked sweet potatoes': '1', 'vegetable wrap': '1', 'tofu': '1', 'black beans patty': '1', 'sautéed spinach and tomatoes': '1', 'roasted potatoes': '1', 'green beans potatoes': '1', 'smoked turkey': '1', 'corn pudding': '1', 'fruit salsa': '1', 'teriyaki sauce': '1', 'veggie pizza': '1', 'tuna and noodles': '1', 'vegetable rice': '1', 'roasted tilapia': '1', 'roasted salmon': '1', 'beef stew': '1', 'bean burrito bowl': '1', 'chicken tetrazzini': '1', 'sweet and sour pork': '1', 'black beans salad': '1', 'lentils': '1', 'Pico Del Gallo': '1', 'Black beans and Rice': '1', 'Yucca': '1', 'Vegetable soup': '1', 'Baked lentils': '1', 'Broiled Tomatoes and cheese': '1', 'Grapes': '1', 'Lettuce': '1', 'Mushrooms': '1', 'Carrots': '1', 'Capsicum': '1', 'Spring onions': '1', 'Guacamole': '1', 'Green onion omelet': '1', 'Raisin muffin': '1', 'Pumpkin soup': '1', 'Garden pasta salad': '1', 'Tomato salsa': '1', 'Baked fish': '1', 'Chicken casserole': '1', 'Chicken salad': '1', 'Veggie burger': '1', 'Meatloaf': '1', 'Bacon': '0', 'Cake': '0', 'Cheese': '0', 'Cookies': '0', 'Donuts': '0', 'Energy drinks': '0', 'Fruit drinks': '0', 'Hot dogs': '0', 'Pastry': '0', 'Pizza': '0', 'Soda': '0', 'Beer': '0', 'Sausage': '0', 'Margarine': '0', 'Fried chicken': '0', 'Fish and chips': '0', 'Fried fish': '0', 'French fries': '0', 'Pancakes': '0', 'Microwave popcorns': '0', 'Ketchup': '0', 'Onion rings': '0', 'Bread': '0', 'Vegetable oil': '0', 'Flying Gorilla drink': '0', 'Chocolate cake': '0', 'Cheese curd bacon burger with fries': '0', 'Cheeseburger omelette with pancakes': '0', 'Ultimate smokehouse combo': '0', 'Fried Steak': '0', 'Chicken Tenders': '0', 'Thai Curry Boneless Wings': '0', 'Fettuccine Weesie': '0', 'Bacon Ranch Beef Quesadilla': '0', 'Hash Browns': '0', 'Pad Thai Shrimp': '0', 'Macaroni Grill Chicken Parmesan': '0', 'Crispy Chicken Mac ‘N Cheese': '0', 'BBQ’n Burger': '0', 'Chicken Pot Pie': '0', 'Jalapeño Thickburger': '0', 'Arby’s': '0', 'Baskin Robins': '0', 'Bonjangles': '0', 'Boston Market': '0', 'Burger King': '0', 'Captain Ds': '0', 'Carls Jr.': '0', 'Checkers': '0', 'Chick-fil-A': '0', 'Chipotle': '0', 'Churchs Chicken': '0', 'CiCis Pizza': '0', 'Culvers': '0', 'Dairy Queen': '0', 'Del Taco': '0', 'Dominos Pizza': '0', 'Dunkin Donuts': '0', 'Einstein Bros.Bagels': '0', 'El Pollo Loco': '0', 'Five Guys Burger & Fries': '0', 'Hardees': '0', 'In-N-Out Burger': '0', 'Jack in the box': '0', 'Jasons Deli': '0', 'Jimmy Johns': '0', 'KFC': '0', 'Krispy Kreme': '0', 'Krystal': '0', 'Little Caesars': '0', 'Long John Silvers': '0', 'McDonalds': '0', 'Panda Express': '0'}



        for line in fileinput.input(text, inplace=False):
            line = line.rstrip()
            final_result = defaultdict(int)
            if not line:
                    continue
            for f_key, f_value in fields.items():

                    if (f_key in line) and f_value== '1':

                        final_result['healthy']+=1
                    elif (f_key in line) and f_value== '0':
                        final_result['unhealthy'] +=-1


            #try:
            if final_result['healthy'] != 0 or final_result['unhealthy'] != 0:

                final_result['compound']=( final_result['healthy']+final_result['unhealthy'])/((final_result['healthy'])-(final_result['unhealthy']))

                print('{},final:{}'.format(line,dict(final_result)),file=open("food_sentiment\\food_sentiment.txt", "a"))


                if final_result['compound']>0:
                    #
                     print(line,file=open("food_sentiment\\positive_food_sentiment.txt", "a"))

                elif final_result['compound']<0:
                    print(line, file=open("food_sentiment\\negative_food_sentiment.txt", "a"))

                else:
                    print(line, file=open("food_sentiment\\neutral_food_sentiment.txt", "a"))
                #         #
                # #     #f.write('{}'.join(dict(final_result)))
                #    # print('final:{}'.format(dict(final_result)))#,file=open("validated_results_vader\\texas_unhealthy_vader_pos.csv", "a"))
                # #     print(line, file=open("training_results_vader\\texas_unhealthy_vader_pos.txt", "a"))

            #except ZeroDivisionError:
                 # final_result['compund']==0


obj=food_classify()
obj.food_senti()
