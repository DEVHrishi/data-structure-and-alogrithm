'''
Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))'''

class Solution:

    def preToInfix(self, pre_exp):

        s=[]

        for i in pre_exp[::-1]:

            if i.isalpha():

                s.append(i)

            else:

                a=s.pop()

                b=s.pop()

                s.append("("+a+i+b+")")

        return s[0]