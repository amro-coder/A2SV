class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for u,v in prerequisites:
            graph[v].append(u)
            
        def dfs(node):
            vis[node]=1
            cycle=False
            for child in graph[node]:
                if vis[child]==1:
                    return True
                if vis[child]==0:
                    cycle|=dfs(child)
            vis[node]=2
            ans.append(node)
            return cycle
        vis=[0]*n# 0=not vis, 1=under processing, 2=visited.
        ans=[]
        cycle=False
        for node in range(n):
            if vis[node]==0:
                cycle|=dfs(node)
        ans.reverse()
        return [] if cycle else ans
                    
            
        
        
        