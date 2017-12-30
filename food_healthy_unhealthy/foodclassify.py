# unhealthy = []
# healthy = []
# with open("foodlist.txt", encoding='utf-8') as f:
#     d = {}
#     for line in f:
#         lines1 = line.split(",")
#
#         d[lines1[0]] = lines1[1].strip('\n')
#
#
# filepath = 'vaderresults\\testfile.txt'
# with open(filepath) as fp:
#
#    numlines=0
#    for lines in fp:
#        numlines+=1
#    cnt = 1
#    while len(line)>numlines:
#      print(line)
#
#      cnt += 1

def line_count():
    file1="vaderresults\\testfile.txt"
    file2="foodlist.txt"
    num_lines = 0
    num_lines1=0
    with open(file1) as f1, open(file2) as f2:
        for line1 in f1:
            num_lines += 1
        for line2 in f2:
            num_lines1+=1
    return num_lines,num_lines1


def compare_line():

print(line_count())


