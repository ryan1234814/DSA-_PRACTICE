class Solution:
    def findSum(self, s):
        total=0
        i=0
        while i<len(s):
            if s[i].isdigit():
                num=""
                while i<len(s) and s[i].isdigit():
                    num+=s[i]
                    i+=1
                total+=int(num)
            else:
                i+=1
        return total