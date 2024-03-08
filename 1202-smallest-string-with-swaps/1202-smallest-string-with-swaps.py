class Solution:
    
    def dfs(self,node,visited,graph):
        ans=[]
        stack=[node]
        while stack:
            parent=stack.pop()
            if not visited[parent]:
                visited[parent]=True
                ans.append(parent)
                for child in graph[parent]:
                    if not visited[child]:
                        stack.append(child)
        return sorted(ans)
                
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        # initializing graph
        graph=[[] for _ in range(n)]
        for u,v in pairs:
            graph[u].append(v)
            graph[v].append(u)
            
        # getting the connected components
        connected_compononets=[]
        visited=[False] *n
        for node in range(n):
            if not visited[node]:
                connected_compononets.append(self.dfs(node,visited,graph))
        print(connected_compononets)
                
        # sorting each component
        ans=['']*n
        for c in connected_compononets:
            temp=sorted([s[i] for i in c])
            for i in range(len(c)):
                ans[c[i]]=temp[i]
                
        return ''.join(ans)
            
        
        
                
        
        
        
        