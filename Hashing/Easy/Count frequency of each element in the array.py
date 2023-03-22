def Frequency(arr, n):
    mp = {}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        print(x, mp[x])


if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    Frequency(arr, n)

'''
Time Complexity: O(N)
Space Complexity: O(n)

Input: arr[] = {10,5,10,15,10,5};
Output: 
10  3
5  2
15  1
'''