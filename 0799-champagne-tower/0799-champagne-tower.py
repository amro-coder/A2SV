class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n=101
        dp=[[0]*n for _ in range(n)]
        dp[0][0]=poured
        for i in range(n-1):
            for j in range(n-1):
                dp[i+1][j]+=max((dp[i][j]-1)/2,0)
                dp[i+1][j+1]+=max((dp[i][j]-1)/2,0)
                dp[i][j]=min(dp[i][j],1)
        return dp[query_row][query_glass]
        