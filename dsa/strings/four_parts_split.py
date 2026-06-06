#User function Template for python3

class Solution:
    def isPossible (self, S):
        n=len(S)
        for i in range(1,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    s1=S[0:i]
                    s2=S[i:j]
                    s3=S[j:k]
                    s4=s[k:]
                    if s1!=s2 and s1!=s3 and s1!=s4 and  s2!=s3 and s2!=s4 and s3!=s4:
                        return 1
        return 0
        # code her