# import re
# import unicodedata
# d=open("tweet.txt","a",encoding='UTF-8')
# input =open("dup_tweets_unhealthy123.txt",encoding="UTF-8")
# for c in input:
#
#
#
#     a=re.sub('[\U0001F32C-\U0001F9C0]', lambda y: unicodedata.name(y.group(0)), c)
#     d.write(a)
#     print(a)
import re

# Build a dictionary of replacements:

def emojis():
    fields={}
    with open("list_emojis",'r') as f:
        fields = {}
        for line in f:
            x = line.split(",")
            s = x[0]
            b = x[1]
            fields[s] = b.strip("\n")

    print (fields)


    with open("data\\final.txt",'r') as f:
        for line in f:
            line = line.rstrip()
            # for i in fields:
            for field in fields:
                    field_value = fields[field]

                    if field in line:
                        line = line.replace(field, field_value)

            with open("data\\final1.txt","a") as f:
                f.writelines(line+'\n')
            print line
print emojis()

