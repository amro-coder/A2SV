class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(int(i) for i in deadends)
        target=int(target)
        n=10000
        graph=[[] for _ in range(n)]
        for i in range(n):
            node=str(i)
            node='0'*(4-len(node))+node
            for j in range(4):
                temp=list(node)
                temp[j]=str((int(temp[j])+1)%10)
                child=int(''.join(temp))
                if child not in deadends:
                    graph[i].append(child)
                    
                temp=list(node)
                temp[j]=str((int(temp[j])-1)%10)
                child=int(''.join(temp))
                if child not in deadends:
                    graph[i].append(child)
                    
        ans=[-1]*n
        ans[0]=0
        q=deque([0])
        while q:
            p=q.popleft()
            for c in graph[p]:
                if ans[c]==-1:
                    q.append(c)
                    ans[c]=ans[p]+1
        return -1 if 0 in deadends else ans[target]
        
                    
                    
        
                
        