
f = open("p042_words.txt", 'r')

from datetime import datetime
q = datetime.now()

trilist = []
for n in range(100):
    trilist.append(n*(n+1)/2)

for line in f:
    temp = line
    res = temp.split(",")

count = 0
for word in res:
    temp = word.replace('"', "")
    tempres = 0
    a = ord("A");
    for char in temp:
        tempres += (ord(char)-a+1)
    if tempres in trilist:
#        print temp
        count += 1;
            
print count
print datetime.now() - q
#8ms
f.close();

