import json
def remove_duplicates(infile):
  storehouse = set()
  with open('san_diego_ca.txt', 'w+') as out:
    for line in open(infile):
         if line not in storehouse:
             out.write(line)
             storehouse.add(line)


remove_duplicates('data\\san_diego_ca.txt')
