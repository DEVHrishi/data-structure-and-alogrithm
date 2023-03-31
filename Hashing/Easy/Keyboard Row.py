'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]'''

from ast import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = set("qwertyuiop")
        line2 = set("asdfghjkl")
        line3 = set("zxcvbnm")
        
        return [word for word in words if set(word.lower()).issubset(line1) or 
               set(word.lower()).issubset(line3) or
               set(word.lower()).issubset(line2)]
    
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}
        
        res = []
        for i in words:
            wordset = set(i.lower())
            if (wordset&set1 == wordset) or (wordset&set2 == wordset) or (wordset&set3 == wordset):
                res.append(i)
        return res

