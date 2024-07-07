class Solution:
    def nearestExit(self, mat: List[List[str]], entrance: List[int]) -> int:
        n,m=len(mat),len(mat[0])
        dis=[[-1]*m for _ in range(n)]
        q=deque()
        q.append(tuple(entrance))
        dis[entrance[0]][entrance[1]]=0
        ans=float("inf")
        while q:
            x,y=q.popleft()
            if (x in [0,n-1] or y in [0,m-1]) and [x,y]!=entrance:
                ans=min(ans,dis[x][y])
            for i,j in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if 0<=i<n and 0<=j<m and mat[i][j]=='.' and dis[i][j]==-1:
                    dis[i][j]=dis[x][y]+1
                    q.append((i,j))
        return -1 if ans==float("inf") else ans
