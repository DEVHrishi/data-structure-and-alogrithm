def decrypt(code, k):
        nums = code+code        
        out = []
        if k == 0:
            return len(code)*[0]
        elif k > 0:
            for i in range(len(code)):
                out.append(sum(nums[i+1:i+k+1]))
        else:
            for i in range(len(code), 2*len(code)):                
                out.append(sum(nums[i+k:i]))
        
        return out

print(decrypt([5,7,1,4], 3))