# brute force method
def plusOne(nums):
    arr = ''.join(map(str, nums))
    arr = int(arr) + 1
    return [int(x) for x in str(arr)]

print('plusOne([4,3,2,1]) =', plusOne([4,3,2,1]))

# recursion method tc = O(n) sc = O(1)
def plusOne(self, digits):
        if digits[-1] == 9:
            if len(digits) == 1:  # Already a 9
                return [1, 0]
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        return digits

print('plusOne([4,3,2,1]) =', plusOne([4,3,2,1]))