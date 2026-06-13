class Solution:
    def findEquilibrium(self, arr):
        n=len(arr)
        total_sum=sum(arr)
        left_sum=0
        
        for i in range(n):
            right_sum=total_sum-arr[i]-left_sum
            if left_sum==right_sum:
                return i
            else:
                left_sum+=arr[i]
        return -1