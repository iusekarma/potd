class Solution:
    def isMaxHeap(self,arr,n):
        for i in range(1,n):
            p = ((i+1)//2) - 1
            if arr[i] > arr[p]:
                return False
        return True
