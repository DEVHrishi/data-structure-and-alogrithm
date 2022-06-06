def decompressRLElist(nums):
        a=[]
        for i in range(1,len(nums),2):
            a+=[nums[i]]*nums[i-1]
        return(a)

print(decompressRLElist([1,2,3,4]))