'''Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

 

Example 1:

Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4] 
Explanation: 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
Example 2:

Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
Output: [0,1] 
Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
Example 3:

Input: favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
Output: [0,1,2,3]'''

from ast import List
import collections

# tc: O(n^2) and sc: O(n)
class Solution:
    def peopleIndexes(self, fav: List[List[str]]) -> List[int]:
        res = []
        new_fav = sorted(fav , key = lambda x : len(x)) 
        '''A is subset of B then len(A) < len(B)
        // New List to iterate on lists >= len(fav[i]) to save some iterations'''
        for i in range(len(new_fav)) :
            flag = True 
            '''Intalize it as unique list'''
            for j in range(i+1 , len(new_fav)) :
                '''EX--if len of A is 2 and (A intersection B is) 1
                then A not subsect of B , the intersection must be equal len(A)'''
                if len(set(new_fav[j]).intersection(set(new_fav[i]))) == len(new_fav[i]) :
                    flag = False 
                    break  

            if flag : 
                ''' add to result if it is Unique list'''
                res.append(fav.index(new_fav[i])) 
        res.sort() 
        return res


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        c = collections.defaultdict(set)
        f = favoriteCompanies
        for i in range(len(f)):
            c[i] = set(f[i])
        

        ans = []
        for i in range(len(f)):
            for key in c:
                if key == i :
                    continue
                if c[i] & c[key] == c[i]:
                    break 
            else:
                ans.append(i)
        return ans

