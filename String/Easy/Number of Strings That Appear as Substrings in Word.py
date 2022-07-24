'''Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.'''

def numOfStrings(self, patterns, word: str) -> int:
        return sum(p in word for p in patterns)


def numOfStrings(self, patterns, word: str) -> int:
        ans = 0
        for i in patterns:
            if i in word:
                ans += 1
        return ans