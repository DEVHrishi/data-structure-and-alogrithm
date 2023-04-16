arr = [2,3,5,1,9]
k = 10

# tc = O(n^2) and sc = O(1)
mx = 0
n =len(arr)

for i in range(n):
    s = 0
    for j in range(i, n):
        s += arr[j]
        if s == k:
            mx = max(mx, j - i + 1)
print(mx)

# tc = O(n) and sc = O(1)
def longest_subarray_with_sum(arr, K):
    left = 0
    right = 0
    current_sum = arr[0]
    max_length = 0

    while right < len(arr):
        if current_sum == K:
            max_length = max(max_length, right - left + 1)
            right += 1
            if right < len(arr):
                current_sum += arr[right]
        elif current_sum < K:
            right += 1
            if right < len(arr):
                current_sum += arr[right]
        else:
            current_sum -= arr[left]
            left += 1

    return max_length

# tc = O(n) and sc = O(1)
# Hashing method for both positive and negative numbers
def longest_subarray_with_sum(arr, K):
    prefix_sum = {0: -1}
    current_sum = 0
    max_length = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == K:
            max_length = i + 1
        elif current_sum - K in prefix_sum:
            max_length = max(max_length, i - prefix_sum[current_sum - K])
        if current_sum not in prefix_sum:
            prefix_sum[current_sum] = i

    return max_length
