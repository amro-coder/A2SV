class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        graph=[[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j and (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2 <= bombs[i][2]**2:
                    graph[i].append(j)
        
        def dfs(node):
            ans=1
            vis[node]=True
            for child in graph[node]:
                if not vis[child]:
                    ans+=dfs(child)
            return ans
        
        ans=0
        for node in range(n):
            vis=[False]*n
            ans=max(ans,dfs(node))

        return ans
                