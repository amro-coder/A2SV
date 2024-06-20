class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        visited=[False]*n
        color=[0]*n
        def dfs(node,c):
            color[node]=c
            visited[node]=True
            for child in graph[node]:
                if not visited[child]:
                    dfs(child,1-c)
        for node in range(n):
            if not visited[node]:
                dfs(node,0)
        for node in range(n):
            for child in graph[node]:
                if color[child]==color[node]:
                    return False
        return True
        