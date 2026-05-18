class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            st=""
            for j in range(i,len(s)):
                if s[j] in st:
                    break
                st+=s[j]
            total=max(total,len(st))
        return total
        