class Solution:
    def isStringExist (self, arr, N, S):
        for i in range(N):
          if len(arr[i])==len(S):
              cnt=0
              for j in range(len(S)):
                  if arr[i][j]!=S[j]:
                      cnt+=1
                      if cnt>1:
                          break
              if cnt==1:
                  return True
        return False