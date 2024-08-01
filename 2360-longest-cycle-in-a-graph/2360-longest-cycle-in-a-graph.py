class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n=len(edges)
        vis,num,ans=[n]*n,0,-1
        for node in range(n):
            if vis[node]==n:
                start=num
                while node!=-1 and vis[node]==n:
                    prev=node
                    vis[node]=num
                    num+=1
                    node=edges[node]
                if node!=-1 and vis[node]>=start:
                    ans=max(ans,vis[prev]-vis[node]+1)
        return ans
                
        