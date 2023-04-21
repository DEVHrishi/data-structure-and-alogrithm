'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''

# tc = O(n) and sc = O(1)
class Solution(object):
    def isPalindrome(self, s):
        # Initialize two pointer variables, left and right and point them with the two ends of the input string...
        left, right = 0, len(s) - 1
        # Traverse all elements through the loop...
        while left < right:
            # Move the left pointer to right so it points to a alphanumeric character...
            while left < right and not s[left].isalnum():
                left += 1
            # Similarly move right pointer to left so it also points to a alphanumeric character...
            while left < right and not s[right].isalnum():
                right -= 1
            # Check if both the characters are same...
            # If it is not equal then the string is not a valid palindrome, hence return false...
            if s[left].lower() != s[right].lower():
                return False
            # If same, then continue to next iteration and move both pointers to point to next alphanumeric character till left < right...
            left, right = left + 1, right - 1
        # After loop finishes, the string is said to be palindrome, hence return true...
        return True

# tc = O(n) and sc = O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''
        for i in s:
            if i.isalnum():
                x = x + i
        x= x.lower()
        x_rev = x[::-1]
        return(x == x_rev)
           