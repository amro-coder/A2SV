class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n,m=len(grid),len(grid[0])
        for i in range(n):
            grid[i]=list(grid[i])
        
        def solve(order,x,y,grid):
            ans=0
            inventory=set()
            for val,destx,desty in order:
                dis=[[-1]*m for _ in range(n)]
                dis[x][y]=0
                q=deque([(x,y)])
                while q:
                    px,py=q.popleft()
                    for i,j in [(px-1,py),(px+1,py),(px,py-1),(px,py+1)]:
                        if 0<=i<n and 0<=j<m and dis[i][j]==-1 and (grid[i][j] in ['.','@'] or grid[i][j].islower() or grid[i][j] in inventory):
                            q.append((i,j))
                            dis[i][j]=dis[px][py]+1
                if dis[destx][desty]==-1:
                    return float("inf")
                
                inventory.add(val.capitalize())
                
                ans+=dis[destx][desty]
                x,y=destx,desty                        
            return ans
            
        
        keys=[]
        x,y=-1,-1
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='@':
                    x,y=i,j
                if grid[i][j].islower():
                    keys.append((grid[i][j],i,j))
        ans=float("inf")
        for perm in permutations(keys):
            ans=min(solve(perm,x,y,deepcopy(grid)),ans)
            
        return ans if ans!=float("inf") else -1
            
        
                    
            