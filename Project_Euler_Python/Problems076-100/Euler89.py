# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 12:50:42 2016

@author: Home
"""

from datetime import datetime
startTime = datetime.now()
#print datetime.now() - startTime


dec_arr = []
pre_char_count = 0

NtoD = {}
NtoD['I'] = 1
NtoD['V'] = 5
NtoD['X'] = 10
NtoD['L'] = 50
NtoD['C'] = 100
NtoD['D'] = 500
NtoD['M'] = 1000

DtoN = {}
DtoN[1] = 'I'
DtoN[4] = 'IV'
DtoN[5] = 'V'
DtoN[9] = 'IX'
DtoN[10] = 'X'
DtoN[40] = 'XL'
DtoN[50] = 'L'
DtoN[90] = 'XC'
DtoN[100] = 'C'
DtoN[400] = 'CD'
DtoN[500] = 'D'
DtoN[900] = 'CM'
DtoN[1000] = 'M'


d_keys = DtoN.keys()
d_keys.sort()
d_keys.reverse()

#%%
f = open("p089_roman.txt", 'r')

for walk in f:
    line = walk.replace("\n", "")
    res = 0
    pre_char_count += len(line)
    for i in range(len(line)-1):
        if NtoD[line[i]] < NtoD[line[i+1]]:
            res -= NtoD[line[i]]
        else:
            res += NtoD[line[i]]
    res += NtoD[line[-1]]
    dec_arr.append(res)
    
f.close()

#%%
N_arr = []
post_count = 0
for dec in dec_arr:
    decode = dec
    res_str = ""
    while decode != 0:
        for n in d_keys:
            if n <= decode:
                res_str += DtoN[n]
                decode -= n
                break
    
    N_arr.append(res_str)
    post_count += len(res_str)
    
#%%

print "Amount of characters saved = " + str(pre_char_count - post_count)
print datetime.now() - startTime
#time: 14ms

