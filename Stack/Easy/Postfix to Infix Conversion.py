'''
Input:
ab*c+ 
Output: 
((a*b)+c)'''

class Solution:
    def postToInfix(self, postfix):
        # Code here
        s=[] 

        for i in postfix:

            if i.isalpha():

                s.append(i)

            else:

                b=s.pop()

                a=s.pop()

                s.append("("+a+i+b+")")

        return s[0]