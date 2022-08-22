'''Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].'''

def sumZero(self, n: int):
        l=[]
        for i in range(0,n//2):
            l.append(-(i+1))
            l.append(i+1)
        if n%2==1:
            l.append(0)
        return l