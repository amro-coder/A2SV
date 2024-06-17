class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans=float("inf")
        current=[0]*k
        def backtrack(start):
            nonlocal ans
            if start==len(cookies):
                ans=min(ans,max(current))
                return
            for i in range(k):
                current[i]+=cookies[start]
                backtrack(start+1)
                current[i]-=cookies[start]
            return
        current[0]+=cookies[0]
        backtrack(1)
        return ans
        