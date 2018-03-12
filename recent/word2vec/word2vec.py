from pyspark import SparkContext, SparkConf
from pyspark.mllib.feature import Word2Vec

# conf = SparkConf().setAppName('MyFirstStandaloneApp')
sc = SparkContext(master="local",appName="SparkDemo")

inp = sc.textFile("clean_tweets\\clean_emojis_unhealthy_tweets.txt").map(lambda row: row.split(" "))

word2vec = Word2Vec()
model = word2vec.fit(inp)
term=['friedrice','springroll','bacon','cake','cheese','cookie','donut','energydrink','fruitdrink','hotdog','pastry','pizza','soda','beer','sausage','margarine','friedchicken','fishandchip','friedfish','frenchfries','potato','churros','pancake','popcorns','ketchup','onionrings','bread','vegetableoil','flyinggorilladrink','chocolatecake','bacon','nuggets','cheesecurdbaconburgerwithfries','cheeseburgeromelettewithpancakes','ultimatesmokehousecombo','friedsteak','chickentender','thaicurrybonelesswings','fettuccineweesie','baconranchbeefquesadilla','hashbrowns','padthaishrimp','macaronigrillchickenparmesan','crispychickenmacncheese','bbqnburger','chickenpotpie','jalapenothickburger','arbys','baskinrobins','bonjangles','bostonmarket','burgerking','captainds','carlsjr','checkers','chickfila','chipotle','churchschicken','cicispizza','culvers','dairyqueen','deltaco','dominospizza','dunkindonuts','einsteinbrosbagels','elpolloloco','fiveguysburger&fries','hardees','innoutburger','jackinthebox','jasonsdeli','jimmyjohns','kfc','krispykreme','krystal','littlecaesars','longjohnsilvers','mcdonalds','pandaexpress','creamgravy','cheesesauce','dessert','friedsweetapples','wine','milkshake','chips','pepperoni']

for items in term:
  synonyms = model.findSynonyms(items, 5)
  print(items,synonyms)
  f=open("word2vec\\unhealthy_emotion_word2vec.txt", "a")
  f.write("%s %s\n" %(items,synonyms))





# for word, cosine_distance in synonyms:
#          print("{}: {}".format(word, cosine_distance))