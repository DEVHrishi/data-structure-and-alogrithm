'''A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false'''

import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        al = list(string.ascii_lowercase)
        for i in al:
            if i not in sentence:
                return False
                break
        else:
            return True
        
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # in Python, a set can automatically be constructed
        # from iterables such as strings, lists, ...
        return len(set(sentence)) == 26