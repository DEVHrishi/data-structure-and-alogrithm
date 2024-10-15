class Solution:

    def heapify(self,arr,n,ind):

        target=ind

        left=2*ind+1

        right=2*ind+2

        if left<len(arr) and arr[target]<arr[left]:

            target=left

        if right<len(arr) and arr[target]<arr[right]:

            target=right

        if target!=ind:

            arr[ind],arr[target]=arr[target],arr[ind]

            self.heapify(arr,n,target)

        

    def convertMinToMaxHeap(self, N, arr):

        for i in range(N//2-1,-1,-1):

            self.heapify(arr,N,i)

        return arr