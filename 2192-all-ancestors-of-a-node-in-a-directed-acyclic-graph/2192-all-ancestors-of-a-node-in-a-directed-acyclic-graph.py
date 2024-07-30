class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:  
        def bfsTopoSort():# it preforms worse than the dfs one when the graph is sparse
            q = deque([node for node in range(n) if in_degree[node] == 0])
            ans = []
            while q:
                p = q.popleft()
                ans.append(p)
                for child in graph[p]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        q.append(child)
            return ans
        
        in_degree = [0]*n
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            in_degree[v]+=1
            
        toposort=bfsTopoSort()
        
        ans=[set() for _ in range(n)]
        for node in toposort:
            for child in graph[node]:
                ans[child]=ans[child].union(ans[node])
                ans[child].add(node)
        for node in range(n):
            ans[node]=sorted(ans[node])
        return ans
            
        
        