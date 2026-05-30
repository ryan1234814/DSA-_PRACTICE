class Solution:
    def firstOccurence(self,txt,pat):
        for i in range(len(txt)-len(pat)+1):
            for j in range(len(pat)):
                if txt[i+j]!=pat[j]:
                    break
                if j==len(pat)-1:
                    return  i
        return -1
            