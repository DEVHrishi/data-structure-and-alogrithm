'''Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.'''

def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        if k == 0:
            # Quick acception when k = 0
            return True
        
		
		
        # record previous index of 1
        prev_position = None

        for idx, number in enumerate(nums):
            
            if number == 1:
                
                if ( prev_position is not None ) and (idx - prev_position) <= k:
                    # Reject when distance to previous 1 is too close
                    return False
                
                prev_position = idx
        
        # Accept if all 1s are separated of distance k
        return True