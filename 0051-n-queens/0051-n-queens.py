class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_attackable(x,y):
            ans=set([(i,y) for i in range(n)]+[(x,i) for i in range(n)])
        
            i,j=x,y
            while 0<=i<n and 0<=j<n:
                ans.add((i,j))
                i,j=i+1,j+1
            
            i,j=x,y
            while 0<=i<n and 0<=j<n:
                ans.add((i,j))
                i,j=i-1,j-1
            
            i,j=x,y
            while 0<=i<n and 0<=j<n:
                ans.add((i,j))
                i,j=i-1,j+1
            
            i,j=x,y
            while 0<=i<n and 0<=j<n:
                ans.add((i,j))
                i,j=i+1,j-1
                
            return ans
        
        ans=[]
        def backtrack(grid,vis,row):
            if row==n:
                ans.append(grid)
                return
            for col in range(n):
                if (row,col) not in vis:
                    temp_grid=deepcopy(grid)
                    temp_grid[row][col]="Q"
                    backtrack(temp_grid,vis.union(get_attackable(row,col)),row+1)
        backtrack([['.']*n for _ in range(n)],set(),0)
        for temp in ans:
            for i in range(len(temp)):
                temp[i]=''.join(temp[i])
        return ans
    
                        
                    
            
        