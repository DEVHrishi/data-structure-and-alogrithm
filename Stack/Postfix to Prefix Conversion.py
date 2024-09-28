'''
Input: 
ABC/-AK/L-*
Output: 
*-A/BC-/AKL'''

class Solution:
    def postToPre(self, post_exp):
        # Code here
        s = []
        for i in post_exp:
            if i.isalpha():
                s.append(i)
            else:
                b = s.pop()
                a = s.pop()
                s.append(i+a+b)
        return s[0]