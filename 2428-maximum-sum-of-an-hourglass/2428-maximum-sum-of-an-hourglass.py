class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if i+1<n and i-1>-1 and j+1<m and j-1>-1:
                    ans=max(ans,sum(grid[i-1][j-1:j+2])+grid[i][j]+sum(grid[i+1][j-1:j+2]))
        return ans
        