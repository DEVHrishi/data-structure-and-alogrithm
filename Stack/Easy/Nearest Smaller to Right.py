'''
arr = [3, 9, 4, 7, 5, 8, 10]
op: [4, 4, 4, 5, -1, -1, -1]
'''

def find_nearest_smaller_to_right(arr):
    stack = []
    result = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(arr[i])

    result.reverse()
    return result
