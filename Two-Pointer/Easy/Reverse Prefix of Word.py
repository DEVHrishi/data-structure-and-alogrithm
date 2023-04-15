'''Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

 

Example 1:

Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
Example 2:

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
Example 3:

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".'''

# tc = O(n) and sc = O(n)
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        w = ''
        for i in range(len(word)):
            if word[i] == ch:
                l = list(word[:i+1])
                x = 0
                y = len(l) - 1
                while(x < y):
                    l[x], l[y] = l[y], l[x]
                    x += 1
                    y -= 1
                w = w + (''.join(l))
                w = w + word[i+1:]
                return w
        else:
            return word

# tc = O(n) and sc = O(n)    
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        w = ''
        for i in range(len(word)):
            if word[i] == ch:
                l = word[:i+1][::-1]
                w = w + l
                w = w + word[i+1:]
                return w
        else:
            return word