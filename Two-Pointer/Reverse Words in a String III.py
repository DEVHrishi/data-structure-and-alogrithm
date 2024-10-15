'''Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"'''

# tc = O(n*m) and sc = O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(len(l)):
            l[i] = l[i][::-1]
        return ' '.join(l)

# tc = O(n*m) and sc = O(n+m)
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()                   #Converting s into a list to get rid of spaces
        out = []
        for word in s:                          #Reversing each word of the list using two-pointers
            i = 0
            j = (len(word) - 1)
            while (i < j):
                word = list(word)
                word[i], word[j] = word[j], word[i]
                i += 1
                j -= 1
            a = (''.join(word))
            out.append(a)
        return(' '.join(out))                     #joining the words back to form a string
