class Solution:
    def minFallingPathSum(self, x: List[List[int]]) -> int:
        n=len(x)
        dp=[[0]*n for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]=x[i][j]+min(float("inf") if j-1<0 else dp[i+1][j-1],dp[i+1][j],float("inf") if j+1>=n else dp[i+1][j+1])        
        return min(dp[0])
    
        