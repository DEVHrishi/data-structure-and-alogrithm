'''In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
    def search(self, word):
        node = self.root
        prefix = ''
        for char in word:
            if char not in node.children: 
                break
            prefix += char
            node = node.children[char]
            if node.isEndOfWord:
                return prefix
        return '' if not node.isEndOfWord else prefix
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        new_sentence = sentence.split(' ')
        for i in range(len(new_sentence)):
            w = self.search(new_sentence[i])
            if w != '':
                new_sentence[i] = w
        return ' '.join(new_sentence)