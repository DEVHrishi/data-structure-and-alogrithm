'''Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"'''

class Solution:
    def traverse(self, str1, str2, memo):
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                if i == 0 or j == 0:
                    memo[i][j] = i + j
                elif str1[i-1] == str2[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])
    def construct_str(self, str1, str2, memo):
        i, j = len(str1), len(str2)
        result = []
        
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])
                i -= 1
                j -= 1
            elif memo[i-1][j] < memo[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -= 1
        
        # Add remaining characters from both strings
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        
        return ''.join(result[::-1])

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = [[-1]*(len(str2)+1) for _ in range(len(str1)+1)]
        self.traverse(str1, str2, memo)
        print(memo)
        return self.construct_str(str1, str2, memo)