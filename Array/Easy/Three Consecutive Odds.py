def threeConsecutiveOdds(arr):
        c = 0
        for i in arr:
            if i % 2 != 0:
                c += 1
            else:
                c = 0
            
            if c == 3:
                return True
        else:
            return False

print(threeConsecutiveOdds([2,6,4,1,3,5]))