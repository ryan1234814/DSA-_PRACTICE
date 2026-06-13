#User function Template for python3

class Solution:
    def stringSort (self,s):
        up=[]
        lo=[]
        for i in s:
            if i.isupper():
                up.append(i)
            else:
                lo.append(i)
        up.sort()
        lo.sort()
        li=[]
        ans=[]
        i=j=0
        while i<len(up) and j<len(lo):
            li.append(up[i])
            li.append(lo[j])
            i+=1
            j+=1
        while i<len(up):
            li.append(up[i])
            i+=1
        while j<len(lo):
            li.append(lo[j])
            j+=1
        return ''.join(li)
        # your code here
        