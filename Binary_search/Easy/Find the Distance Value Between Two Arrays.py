'''Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1'''

from ast import List

# tc = O(m * n) and sc = O(1)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_value = 0

        for num1 in arr1:
            found = False
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    found = True
                    break
            if not found:
                distance_value += 1

        return distance_value

# tc = O(m * log n) and sc = O(1)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance = len(arr1)
        for num in arr1:
            start = 0
            end = len(arr2) - 1
            while start <= end:
                mid = (start+end)//2
                if abs(num- arr2[mid]) <= d:
                    distance -= 1
                    break
                elif arr2[mid] > num :
                    end = mid-1
                elif arr2[mid] < num :
                    start = mid+1
        return distance

# tc = O((m + n) log n) and sc = O(1)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        distance_value = 0

        for num1 in arr1:
            closest_num = self.closest_element(arr2, num1)
            if abs(num1 - closest_num) > d:
                distance_value += 1

        return distance_value

    def closest_element(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return arr[mid]
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if left == 0:
            return arr[left]
        if left == len(arr):
            return arr[right]

        return arr[left] if abs(arr[left] - target) < abs(arr[right] - target) else arr[right]