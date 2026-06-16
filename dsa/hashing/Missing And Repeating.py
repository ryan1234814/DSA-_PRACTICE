class Solution:
    def findTwoElement(self, arr):
        freq=[0]*(len(arr)+1)
        for i in arr:
            freq[i]+=1
        re=-1
        miss=-1
        for i in range(1,len(arr)+1):
            if freq[i]==2:
                re=i
            elif freq[i]==0:
                miss=i
        return [re,miss]