class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid),len(grid[0])
        visited=[[False]*m for _ in range(n)]
        def dfs(r,c):
            visited[r][c]=True
            for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=x<n and 0<=y<m and grid[x][y]=='1' and not visited[x][y]:
                    dfs(x,y)
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and not visited[i][j]:
                    dfs(i,j)
                    ans+=1
        return ans
                    