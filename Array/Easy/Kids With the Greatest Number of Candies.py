'''There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.'''

def kidsWithCandies(candies, extraCandies):
    max_el = max(candies)
    arr = []
    
    for i in range(len(candies)):
        if candies[i] + extraCandies >= max_el:
            arr.append(True)
        else :
            arr.append(False)
    return arr

print(kidsWithCandies([4,2,1,1,2], 1))

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
	maxCandies = max(candies)
	result = []
	for i in range(len(candies)):            
		result.append(candies[i]+extraCandies >= maxCandies)            
	return result
    

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
	maxCandies = max(candies)
	return [candy+extraCandies >= maxCandies for candy in candies]