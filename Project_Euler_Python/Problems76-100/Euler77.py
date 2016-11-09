# -*- coding: utf-8 -*-

from datetime import datetime
startTime = datetime.now()

from eulerTools import sieve_for_primes_to
max_size = 300
max_n = 300

nArray = [0 for i in range(max_size+1)]
nArray[0] = 1
over = sieve_for_primes_to(max_n)

oldArr = nArray
for n in over:
        
    for idx in range(n, max_size):
        nArray[idx] = nArray[idx] + nArray[idx-n]

def binFind_g(arr, idx, n, el):
    if arr[idx] <= el:
        return binFind_g(arr, (n+idx+1)/2, n, el)
    if arr[idx] > el and arr[idx-1] > el: #under assumption element will not be at index 0
        return binFind_g(arr, idx/2, idx, el)
    else:
        return idx

print "smallest number is: " + str(binFind_g(nArray, 0, len(nArray)-1, 5000))

print datetime.now() - startTime
#time: 3ms

