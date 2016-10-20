# -*- coding: utf-8 -*-
from datetime import datetime
q = datetime.now()
meest = 354294
res = []

for i in range(2,meest+1):
    word = str(i)
    temp = 0
    for letter in word:
        temp += (int(letter))**5
    if temp == i:
        res.append(i)

print sum(res)
print datetime.now() - q
