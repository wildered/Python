# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 21:48:32 2017

@author: Home
"""

"""First we seperate the words based on length. Then, going by length,
we look for anagrams. Should we find any, we will check if we can form
a valid 'anagram word pair'. Obviously, the validity of the pair will
be symmetric.
Whilst we can improve the time by around 33% if start with the
longest words, and break once we have the maximum number of that 
length, we could stop, as numbers of lower length will have a lower
value. However, the problem explicitly states 
"find all the square anagram word pairs". """

from math import sqrt, ceil
from datetime import datetime
startTime = datetime.now()

f = open('p098_words.txt', 'r')

words = f.read().split(',')
for i in xrange(len(words)):
    words[i] = words[i].replace('"', '')

f.close()

min_l = len(min(words, key = lambda x: len(x)))
max_l = len(max(words, key = lambda x: len(x)))

words_by_length = []
for i in range(max_l+1):
    words_by_length.append([])

for word in words:
    words_by_length[len(word)].append(word)


sq_map = []
sq_by_length = []
sq_set_by_length = []
for i in range(max_l+1):
    sq_map.append([])
    sq_by_length.append([])
    sq_set_by_length.append(set())


def check_anagram(string1, string2):
    "We can assume the lengths are equal"
    d1, d2 = {}, {}
    s1 = set(string1)
    s2 = set(string2)
    if s1 != s2:
        return False
    for c in s1:
        d1[c] = 0
        d2[c] = 0
    for idx in range(len(string1)):
        d1[string1[idx]] += 1
        d2[string2[idx]] += 1
    return (d1 == d2)

def validator(string, number):
    number = str(number)
    translation_dic = {}
    for idx, c in enumerate(string):
        if c not in translation_dic:
            translation_dic[c] = number[idx]
        else:
            if translation_dic[c] != number[idx]:
                return False, None
    return True, translation_dic
        
def translate_string(string2, trans_dic):
    return int("".join([trans_dic[c] for c in string2]))

def square_finder(string1, string2):

    k = len(string1)
    s1 = set(string1)
    if len(s1) > 10:
        return []
    if sq_by_length[k] == []:
        sq_by_length[k] = [kt*kt for kt in range(int(ceil(sqrt(10**(k-1)))), int(ceil(sqrt(10**(k)))))]
        for sq in sq_by_length[k]:
            sq_set_by_length[k].add(sq)
            sq_map[k].append(set(str(sq)))
    sqList = sq_by_length[k]
    #only mapping to word1
    res_pairs = []
    sq_set = sq_set_by_length[k]
    for idx, square in enumerate(sqList):
        if len(set(string1)) != len(sq_map[k][idx]):
            continue
        flag, trans_dic = validator(string1, square)
        if flag:
            number2 = translate_string(string2, trans_dic)
            if number2 in sq_set:
                res_pairs.append((square, number2))
    return res_pairs
                
            
def find_anagrams(wordList):
    res = []
    for idx in range(len(wordList)-1):
        word1 = wordList[idx]
        for bdx in range(idx + 1, len(wordList)):
            word2 = wordList[bdx]
            if check_anagram(word1, word2):
                pair_arr = square_finder(word1, word2)
                res.extend(pair_arr)
    return res
                
            
pairs_array = []
for length in range(min_l, max_l + 1):
    word_arr = words_by_length[length]
    temp_pairs = find_anagrams(word_arr)
    pairs_array.extend(temp_pairs)
    

largest_square_pair = max(pairs_array, key = lambda x: max(x))
largest_square = max(largest_square_pair)

print "Result = " + str(largest_square)
print datetime.now() - startTime
#time: 0.43s


