'''Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]'''

from ast import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            if len(set(pattern)) == len(set(word)):
                tempDict = {}
                Flag = False
                for i in range(len(pattern)):
                    if pattern[i] not in tempDict:
                        Flag= True
                        tempDict[pattern[i]] = word[i]
                    elif pattern[i] in tempDict and tempDict[pattern[i]] != word[i]:
                        Flag = False
                        break
                if Flag== True:
                    result.append(word)
        return result
        