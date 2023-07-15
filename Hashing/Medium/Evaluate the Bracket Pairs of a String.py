'''Google
2
1807. Evaluate the Bracket Pairs of a String
Medium
436
36
Companies
You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:

Replace keyi and the bracket pair with the key's corresponding valuei.
If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).
Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

Return the resulting string after evaluating all of the bracket pairs.

 

Example 1:

Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".
Example 2:

Input: s = "hi(name)", knowledge = [["a","b"]]
Output: "hi?"
Explanation: As you do not know the value of the key "name", replace "(name)" with "?".
Example 3:

Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
Output: "yesyesyesaaa"
Explanation: The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.'''

import re
from ast import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for i in knowledge:
            d[i[0]] = i[1]
        temp = ''
        res = ''
        flag = 0
        for i in s:
            if i == '(':
                flag = 1
            elif i != ')' and flag == 1:
                temp = temp+i
            elif i == ')':
                if temp in d.keys():
                    res = res+d[temp]
                else:
                    res = res+'?'
                temp = ''
                flag = 0
            else:
                res = res+i
        return res


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Transform the list into a dictonary for quick lookups.
        knowledge = {k[0]: k[1] for k in knowledge}

        # Lookup function taking a Match object returning either the
        # value associated with a matched key or '?' if no such key exists.
        def lookup(match: re.Match) -> str:
            return knowledge.get(match.group(0)[1:-1], '?')

            # Regular expression substitition - pattern lazily looks for zero
            # or more characters between parentheses.
        return re.sub(r"\(.*?\)", lookup, s)
    
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        K = { k[0] : k[1] for k in knowledge}
        stack = []
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                word = []
                while stack[-1] != '(':
                    word.append(stack.pop())
                stack.pop()
                stack.append(K.get(''.join(word[::-1]), '?'))
                
        return ''.join(stack)
