'''A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]'''
'''tc = O(m+n), sc = O(m+n)'''
from ast import List
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        h = Counter((s1.split()) + (s2.split()))
        return [i for i, j in h.items() if j == 1]
    

def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    string1 = list(s1.split(' '))
    string2 = list(s2.split(' '))
    string = string1 + string2
    result = []
    for s in string:
        if string.count(s) == 1:
            result.append(s)
    return result