# -*- coding: utf-8 -*-
text =open("dup_clean_disease.txt",'r')
text=text.read()
text=text.lower()

bigrams = ['eating disorder','food allergy','oral cancer','thyroid cancer','skin cancer','prostate cancer','pancreatic cancer','ovarian cancer','lung cancer','liver cancer','kidney cancer','colorectal cancer','cervical cancer','bladder cancer','brain cancer','breast cancer','brain cancer','heart disease','heart attack','renal failure','kidney disease','fatty liver','intestinal failure','liver disease','lynch syndrome','pancreatic cancer','bleeding disorder','acute coronory syndrome','blood pressure','congestive heart failure','hypertension','pulmonary hypertension''vascular disease',]
for bigram in bigrams:
    text = text.replace(bigram, bigram.replace(" ","_"))
    print (text)
    file=open ("dup_clean_disease1.txt","w")
    file.write(text)

