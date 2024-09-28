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