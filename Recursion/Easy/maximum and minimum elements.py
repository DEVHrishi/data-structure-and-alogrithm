n = [1,2,4,6]

def max_min(n):
    global mx, mn
    mx = mn = n[0]
    def helper(n, x):
        global mx, mn
        if x == 0:
            return mx, mn
        else:
            if n[x-1] > mx:
                mx = n[x-1]
            elif n[x-1] < mn:
                mn = n[x-1]
            return helper(n , x-1)
    return helper(n, len(n))

mx, mn = max_min(n)
print("Max:", mx, "Min:", mn)