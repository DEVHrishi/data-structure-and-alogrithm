'''Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

 

Example 1:

Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
 
Example 2:
Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0 '''

from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    # This will store the indices of negative integers
    dq = deque()
    
    # This will store the result for each window
    result = []
    
    # Process the first window (first K elements)
    for i in range(K):
        if A[i] < 0:
            dq.append(i)
    
    # Process the remaining windows
    for i in range(K, N):
        # If deque is not empty, then the front element is the first negative integer
        if dq:
            result.append(A[dq[0]])
        else:
            result.append(0)
        
        # Remove the elements which are out of this window
        while dq and dq[0] <= i - K:
            dq.popleft()
        
        # Add the current element if it is negative
        if A[i] < 0:
            dq.append(i)
    
    # Add the answer for the last window
    if dq:
        result.append(A[dq[0]])
    else:
        result.append(0)
    
    return result