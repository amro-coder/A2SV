class Solution:
    def findNumberOfLIS(self, x: List[int]) -> int:
        n=len(x)
        dp=[1]*n
        cnt=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if x[i]<x[j]:
                    if 1+dp[j]==dp[i]:
                        cnt[i]+=cnt[j]
                    if 1+dp[j]>dp[i]:
                        dp[i]=1+dp[j]
                        cnt[i]=cnt[j]
        longest=max(dp)
        return sum([cnt[i] for i in range(n) if dp[i]==longest])