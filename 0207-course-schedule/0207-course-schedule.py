class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(n)]
        for u,v in prerequisites:
            graph[v].append(u)
        visited=[0]*n
        def dfs(node):
            if visited[node]==1:
                return False
            visited[node]=1 # node is under processing
            ans=True
            for child in graph[node]:
                if visited[child]!=2:
                    ans&=dfs(child)
            visited[node]=2
            return ans
        ans=True
        for node in range(n):
            if visited[node]==0:
                ans&=dfs(node)
        return ans
            