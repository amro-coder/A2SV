class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        in_degree=[0]*n
        for u,v in prerequisites:
            graph[v].append(u)
            in_degree[u]+=1
        
        q=deque([node for node in range(n) if in_degree[node]==0])
        ans=[]
        while q:
            p=q.popleft()
            ans.append(p)
            for child in graph[p]:
                in_degree[child]-=1
                if in_degree[child]==0:
                    q.append(child)
        return [] if len(ans)<n else ans
                    
            
        
        
        