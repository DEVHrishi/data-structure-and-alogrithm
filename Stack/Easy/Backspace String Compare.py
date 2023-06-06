'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".'''

from ast import List
import itertools

# tc -> O(n), sc -> O(n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(string: str) -> List[str]:
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        processed_s = processString(s)
        processed_t = processString(t)

        return processed_s == processed_t

# tc -> O(n), sc -> O(1)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(string: str) -> List[str]:
            skip = 0
            for i in range(len(string)-1, -1, -1):
                if string[i] == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield string[i]

        return all(x == y for x, y in itertools.zip_longest(processString(s), processString(t)))


