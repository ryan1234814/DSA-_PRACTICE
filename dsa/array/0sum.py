
class Solution:
    def getPairs(self, arr):
        ans=set()
        s=set()
        for i in arr:
            if -i in s:
                ans.add((min(i,-i),max(i,-i)))
            s.add(i)
        
        return sorted(ans)