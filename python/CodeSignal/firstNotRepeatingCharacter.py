'''
Given a string s consisting of small English letters, 
find and return the first instance of a non-repeating character in it. 
If there is no such character, return '_'.

'''
from collections import Counter
def solution(s):
    count = Counter(s)
    for i in s:
        if count[i] == 1: 
            return i
        elif s.index(i) ==s.rindex(i):
            return i
        else:
            return "_"
