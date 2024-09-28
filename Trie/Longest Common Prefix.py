'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.char = ''
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, node):
        if len(node.children) == 1 and not node.is_end_of_word:
            for k, v in node.children.items():
                self.char += k
                self.search(v)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        for s in strs:
            if s == '':
                return ''
            else:
                self.insert(s)
        self.search(self.root)
        return self.char