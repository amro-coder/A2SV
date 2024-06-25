class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n,m=len(grid),len(grid[0])
        def dfs(x,y):
            print(x,y)
            vis[x][y]=True
            if x+1<n and not vis[x+1][y]:
                a=grid[x][y]
                b=grid[x+1][y]
                if 2<=a<=4 and (b==2 or 5<=b<=6):
                    dfs(x+1,y)
                
            if x-1>=0 and not vis[x-1][y]:
                a=grid[x][y]
                b=grid[x-1][y]
                if(a==2 or 5<=a<=6) and 2<=b<=4:
                    dfs(x-1,y)
                    
            if y+1<m and not vis[x][y+1]:
                a=grid[x][y]
                b=grid[x][y+1]
                if(a==1 or a==4 or a==6) and (b==1 or b==3 or b==5):
                    dfs(x,y+1)
            
            if y-1>=0 and not vis[x][y-1]:
                a=grid[x][y]
                b=grid[x][y-1]
                if (a==1 or a==3 or a==5) and (b==1 or b==4 or b==6):
                    dfs(x,y-1)
            return 
        vis=[[False]*m for _ in range(n)]
        dfs(0,0)
        return vis[n-1][m-1]
        
        
                
                    
                
            