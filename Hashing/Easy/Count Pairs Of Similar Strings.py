'''
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

 

Example 1:

Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 
Example 2:

Input: words = ["aabb","ab","ba"]
Output: 3
Explanation: There are 3 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
- i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.
Example 3:

Input: words = ["nba","cba","dba"]
Output: 0
Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.'''

from ast import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if set(words[j]) == set(words[i]):
                    count += 1
        return count
    

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordMap = {}

        #we traverse the input array
        for word in words:
            #convert the word into a (unique characters) hashable key
            #(see notes above for explanation)
            curr = sorted(set(word))
            curr = ''.join(curr)

            #add count of this "similar string" instances
            if curr in wordMap:
                wordMap[curr]+=1
            else:
                wordMap[curr]=1

        pairs = 0
        #traverse through all "similar string" keys
            #and add pairs using the unique combination formula
            #(see notes above for explanation)
        for word in wordMap:
            count = wordMap[word]
            pairs += (count* (count-1))//2

        
        return pairs
        #Time Compelxity: O(N*K)
        #Space Complexity: O(26) -> O(1)
