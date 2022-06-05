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