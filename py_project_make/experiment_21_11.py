# list_sad = [":(", ":-("]
# list_ill=["\ud83d\ude37"]
# list_happy = ["\ud83d\ude00", "\ud83d\ude03"]
#
# a = "im attempt a shepherds pie but i didnt make nearly enough potatoes \ud83d\ude37 smad"
#
# for i in a.split():
#     if i in list_sad:
#         print ("SAD")
#     elif i in list_happy:
#         print ("HAPPY")
#     elif i in list_ill:
#         print("ill")
#     else:
#         print (i)
import re
# word_list = {'\ud83d\ude00' : 'grinning', '\ud83d\ude03' : 'happy','\ud83d\ude04' : 'happy','\ud83d\ude01' : 'grin','\ud83d\ude06' : 'satisfied','\ud83d\ude05' : 'hot','\ud83d\ude02':'joy','\ud83e\udd23':'laughing','\u263a\ufe0f':'pleased','\ud83d\ude0a':'blush','\ud83d\ude07':'innocent','\ud83d\ude42':'smile','\ud83d\ude43':'funny','\ud83d\ude09':'flirt','\ud83d\ude0c':'relieved','\ud83d\ude0d':'love','\ud83d\ude18':'flirt','\ud83d\ude17':'kissing','\ud83d\ude19':'kissing','\ud83d\ude1a':'kissing','\ud83d\ude0b':'yum','\ud83d\ude1c':'silly','\ud83d\ude1d':'prank','\ud83d\ude1b':'stuck out tongue','\ud83e\udd11':'rich','\ud83e\udd17':'hugs','\ud83e\udd13':'nerd','\ud83d\ude0e':'cool','\ud83e\udd21':'clown','\ud83e\udd20':'cowboy','\ud83d\ude0f':'smirk','\ud83d\ude12':'unamused','\ud83d\ude1e':'sad','\ud83d\ude14':'pensive','\ud83d\ude1f':'worried','\ud83d\ude15':'confused','\ud83d\ude41':'frown','\u2639\ufe0f':'frown','\ud83d\ude23':'persevere','\ud83d\ude16':'confounded','\ud83d\ude2b':'tired','\ud83d\ude29':'upset','\ud83d\ude24':'smug','\ud83d\ude20':'angry','\ud83d\ude21':'angry','\ud83d\ude36':'silence','\ud83d\ude10':'neutral','\ud83d\ude11':'expressionless','\ud83d\ude2f':'silence','\ud83d\ude26':'frown','\ud83d\ude27':'stunned','\ud83d\ude2e':'surprise','\ud83d\ude32':'astonished','\ud83d\ude35':'dizzy','\ud83d\ude33':'flushed','\ud83d\ude31':'horror','\ud83d\ude28':'fearful','\ud83d\ude30':'nervous','\ud83e\udd24':'drooling','\ud83d\ude2d':'sob','\ud83d\ude13':'sweat','\ud83d\ude2a':'sleepy','\ud83d\ude34':'sleepy','\ud83d\ude44':'roll eyes','\ud83e\udd14':'thinking','\ud83e\udd25':'liar','\ud83d\ude2c':'grimace','\ud83e\udd10':'silence','\ud83e\udd22':'sick','\ud83e\udd27':'sick','\ud83d\ude37':'sick','\ud83e\udd12':'sick','\ud83e\udd15':'hurt','\ud83d\ude08':'devil','\ud83d\udc7f':'devil','\ud83d\udc79':'monster','\ud83d\udc7a':'monster','\ud83d\udca9':'crap','\ud83d\udc7b':'ghost','\ud83d\udc7b':'danger','\u2620\ufe0f':'danger','\ud83d\udc7d':'alien','\ud83d\udc7e':'space invader','\ud83e\udd16':'robot','\ud83d\ude3a':'smile','\ud83d\ude38':'smile','\ud83d\ude39':'joy','\ud83d\ude3b':'excited','\ud83d\ude3c':'smirk','\ud83d\ude3d':'kissing','\ud83d\ude40':'horror','\ud83d\ude3f':'sad','\ud83d\ude3e':'pouting cat','\ud83d\udc98':'love','\ud83d\udc96':'heart','\ud83d\udc97':'heartbeat','\ud83d\udc93':'heartbeat','\ud83d\udc9e':'twohearts','\ud83d\udc95':'twohearts','\u2763\ufe0f':'heavy heart','\ud83d\udc94':'broken heart','\ud83d\udda4':'black heart','\u2764\ufe0f':'heart','\ud83c\udf89':'hooray','\ud83c\udf8a':'confetti_ball','\ud83c\udf88':'party','\ud83c\udf81':'gift','\ud83d\udecf':'bed','\ud83d\udc92':'marriage','\ud83c\udf7d':'dinner','\ud83c\udf74':'cutlery','\ud83c\udf74':'spoon','\ud83c\udf7e':'celebration','\ud83c\udf79':'vacation','\ud83c\udf78':'drink','\ud83e\udd43':'whisky','\ud83c\udf77':'wine glass','\ud83e\udd42':'toast','\ud83c\udf7b':'beers','\ud83c\udf7a':'beers','\ud83c\udf75':'breakfast','\u2615\ufe0f':'coffee','\ud83c\udf7c':'milk','\ud83e\udd5b':'milk_glass','\ud83c\udf6a':'cookie','\ud83c\udf69':'donut','\ud83c\udf7f':'popcorn','\ud83c\udf6b':'chocolate_bar','\ud83c\udf6c':'candy','\ud83c\udf6d':'lollipop','\ud83c\udf6e':'custard','\ud83c\udf82':'birthday','\ud83c\udf70':'cake','\ud83c\udf66':'icecream','\ud83c\udf68':'icecream','\ud83c\udf63':'sushi','\ud83c\udf4f':'apple','\ud83c\udf4e':'apple','\ud83c\udf50':'pear','\ud83c\udf4a':'orange','\ud83c\udf4b':'lemon','\ud83c\udf4c':'banana','\ud83c\udf49':'watermelon','\ud83c\udf47':'grapes','\ud83c\udf53':'strawberry','\ud83c\udf48':'melon','\ud83c\udf52':'cherries','\ud83c\udf51':'peach','\ud83c\udf4d':'pine apple','\ud83e\udd5d':'kiwi fruit','\ud83e\udd51':'avocado','\ud83c\udf45':'tomato','\ud83c\udf46':'eggplant','\ud83e\udd52':'cucumber','\ud83e\udd55':'carrot','\ud83c\udf3d':'corn','\ud83c\udf36':'spicy','\ud83e\udd54':'potato','\ud83c\udf60':'potatoe','\ud83c\udf30':'chesnut','\ud83e\udd5c':'peanut','\ud83c\udf6f':'honeypot','\ud83e\udd50':'croissant','\ud83c\udf5e':'bread','\ud83e\udd56':'bread','\ud83e\uddc0':'cheese','\ud83e\udd5a':'egg','\ud83c\udf73':'egg','\ud83e\udd53':'bacon','\ud83e\udd5e':'pancakes','\ud83c\udf64':'fried shrimps','\ud83c\udf57':'chicken','\ud83c\udf56':'meat','\ud83c\udf55':'pizza','\ud83c\udf2d':'hot dog','\ud83c\udf54':'hamburger','\ud83c\udf5f':'fries','\ud83e\udd59':'bread','\ud83c\udf2e':'taco','\ud83c\udf2f':'burrito','\ud83e\udd57':'salad','\ud83e\udd58':'curry','\ud83c\udf5d':'pasta','\ud83c\udf5c':'noodles','\ud83c\udf72':'stew','\ud83c\udf65':'fish cake','\ud83e\udd90':'fish'}
# with open("unhealthy_train_pos.txt") as main:
#     with open('unhealthy_train_pos_emoticon.txt', 'w') as new_main:
#         input_data = main.read()
#         for key, value in word_list.iteritems():
#             input_data = input_data.replace(key, value)
#
#         new_main.write(input_data)


def cleaningText(text):
        # The following regex just strips of an URL (not just http), any punctuations,
        # User Names or Any non alphanumeric characters.
        text = text.lower()  # remove capitals
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '.', text)
        # Convert www.* or https?://* to URL
        text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '.', text)
        # Convert @username to AT_USER
        text = re.sub('@[^\s]+', 'AT_USER', text)
        text=re.sub(u"(\u2018|\u2019)", "'", text)
        # Remove additional white spaces
        text = re.sub('[\s]+', ' ', text)
        # Replace #word with word
        text = re.sub(r'#([^\s]+)', r'\1', text)
        return text


with open("healthy_train_neg_emoticon.txt") as t1:
#print(raw_rdd.collect())
    t=[]
    for lines in t1:
    #data = raw_rdd.map(lambda line:line.split("\n"))
           x= cleaningText(lines)

           t.append(x)

    for lines1 in t:
        y=open("train_healthy_neg_clean.txt","a")
        y.write(lines1 +'\n')