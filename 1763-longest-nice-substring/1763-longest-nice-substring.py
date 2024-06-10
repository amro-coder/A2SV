class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(s):
            hashmap=set(s)
            for value in s:
                if value.lower() not in s or value.upper() not in s:
                    return False
            return True
        n=len(s)
        ans=""
        for i in range(n):
            for j in range(i+1,n+1):
                if j-i>len(ans) and is_nice(s[i:j]):
                    ans=s[i:j]
        return ans
                
                
        