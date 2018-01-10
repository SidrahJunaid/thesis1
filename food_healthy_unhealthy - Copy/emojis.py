from __future__ import unicode_literals

#with open("vaderresults\\healthy_vader_neg.txt") as f:
#     for lines in f:
#         words = lines.split()
#         for word in words:
#           if '\u' in word:
#                 print(word)



    # {'u201c':'"','\u2019':',','\u201d':'"','\ud83d\ude44':'face with rolling eyes','\u2026':'...','\u00a1\u00a11':'!!','\ud83d\ude02':'face with tears of joy','\u2018':',','\ud83e\udd22':'nauseated face','\ud83d\ude2d':'loudly crying face','\ud83d\ude22':'crying face','\u2013':'dash','\ud83d\udc16':'pig','\ud83d\ude12':'unamused face','\ud83d\ude04':'laughing','\ud83d\ude42':'smiling','\ud83e\udd26':'face palm','\ud83d\ude22':'cry','\u2014':'dash','\ud83c\udf4c':'banana','\ud83d\ude29':'weary face','\ud83d\udc81\ud83c\udffd':'information desk person','\ud83d\udca9':'poop','\u201ci':',','\u3010':'bracket','\u3011':'bracket':'\ud83e\udd37\ud83c\udffe\u200d\u2642\ufe0f':'shrug','\ud83e\udd24':'drooling','\ud83c\udf4':'not know',}
import re
def food_senti():
    with open("emojis_text.txt") as f:
        fields = {}
        for line in f:
            #line=line.decode('unicode-escape')
            x = line.split(",")

            s = x[1].strip('\n').encode('utf-8').decode('unicode-escape')

            b = x[0]
            fields[s] =b
        print(repr(fields))

    with open("vaderresults\\healthy_vader_neg.txt") as t:
        for line in t:
            line=line.encode('utf-8').decode('unicode-escape')



            for s,b in fields.items():
                    if s in line:
                        line = line.replace(s,b)
            print (line)

food_senti()