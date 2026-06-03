class Solution:
	def twoSum(self, arr, target):
    	    seen=set()
    	    for num in arr:
        	        comp=target-num
        	        if comp in seen:
        	            return True
        	        seen.add(num)
    	    return False