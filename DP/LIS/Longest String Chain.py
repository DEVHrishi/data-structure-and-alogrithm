'''You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.'''

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # Sort words by length
        words.sort(key=len)
        dp = {}
        longest_chain = 1

        for word in words:
            dp[word] = 1  # Initialize each word's chain length as 1
            
            # Check all possible predecessors by removing one character
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)

            # Update the longest chain found so far
            longest_chain = max(longest_chain, dp[word])

        return longest_chain
    
    
class Solution:
    def check(self, words, idx, prev):
        i, j = 0, 0
        p = words[prev]
        c = words[idx]
        if len(c) != len(p) + 1:
            return False  # Ensure the candidate word is exactly one character longer

        count = 0
        while i < len(p) and j < len(c):
            if p[i] != c[j]: 
                count += 1
                if count > 1:
                    return False
                j += 1  # Only increment j to simulate the insertion of one char
            else:
                i += 1
                j += 1

        # If one extra character in `c` is allowed
        return True

    def fun(self, words, idx, prev, memo):
        if idx >= len(words):
            return 0
        if memo[prev + 1][idx] != -1:
            return memo[prev + 1][idx]
        
        pick = 0
        if prev == -1 or self.check(words, idx, prev):
            pick = 1 + self.fun(words, idx + 1, idx, memo)
        skip = self.fun(words, idx + 1, prev, memo)
        
        memo[prev + 1][idx] = max(pick, skip)
        return memo[prev + 1][idx]

    def longestStrChain(self, words: list[str]) -> int:
        n = len(words)
        words = sorted(words, key=len)  # Sort words by length
        
        # Adding an extra row in memo for prev = -1 scenario
        memo = [[-1] * n for _ in range(n + 1)]
        return self.fun(words, 0, -1, memo)