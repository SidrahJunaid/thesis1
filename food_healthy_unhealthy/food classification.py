import csv
from decimal import *

import math, re, string, requests, json
from itertools import product
from inspect import getsourcefile
from os.path import abspath, join, dirname

# for removing punctuation
REGEX_REMOVE_PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))

PUNC_LIST = [".", "!", "?", ",", ";", ":", "-", "'", "\"",
             "!!", "!!!", "??", "???", "?!?", "!?!", "?!?!", "!?!?"]
C_INCR = 0.733

N_SCALAR = -0.74


class SentimentIntensityAnalyzer(object):
   # global d
   # d={}

   def __init__(self):
       self.d = dict()
   def file_read(self):

            with open("foodlist.txt",'r') as file1:


                for lines in file1:
                    x=lines.split(",")
                    word=x[0]
                    measure=x[1].strip()
                    self.d[word]=measure
                return self.d

   def search(self):





worker=SentimentIntensityAnalyzer()
print(worker.search())
# def text_reader():
#     tempList = []
#     foodname = []
#     # read the csv data for parsing
#     with open("foodlist.txt", "r") as f_obj:
#         reader = f_obj.read()
#         for row in reader:
#             tempList.append(row)
#     # parse the list
#     for i in tempList:
#         words = str(i[0]).split(",")
#         foodname.append(words)
#
#     # for testing: print(cerealIngredients)
#     # return to be used in other methods
#     return foodname





