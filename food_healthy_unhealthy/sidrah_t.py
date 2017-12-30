# myDict = {'chicken tikka': '0', 'address':'1',
#       'firstName': '1', 'lastName':'1'}
#
#
# def search(values, searchFor):
#     for k in values:
#         for v in values[k]:
#             if searchFor in k:
#                 return v
#     return None
#
#
# print(search(myDict, 'address'))
#
# number_of_words  = int(input("Enter the number of words. "))
#
# word_dict = {}
#
# for i in range(number_of_words):
#     word =input("Enter word. ")
#     if word in word_dict:
#         word_dict[word] += 1
#     else:
#         word_dict[word] = 1
#
# print (word_dict)
#
# print(sum([len(word)*word_dict[word] for word in word_dict])/number_of_words)
unhealthy=[]
healthy=[]
with open("foodlist.txt",encoding='utf-8') as f:
    d={}
    for line in f:
         lines1=line.split(",")

         d[lines1[0]]=lines1[1].strip('\n')

print(d)


my_list = [line.split(',') for line in open("vaderresults\\healthy_vader_neg.txt")]

for name,age in d.items():
 for a in my_list:

    if a == name:
        healthy.append(1)
    if a== name and age==0:
        unhealthy.append(-1)
total=((len(healthy)-len(unhealthy))/(len(healthy+unhealthy)))


print('healthy:{},unhealthy:{},compund:{}'.format(healthy,unhealthy,total))
print(total)
