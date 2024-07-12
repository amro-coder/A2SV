class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        x,n=[],len(tasks)
        for i in range(n):
            x.append((tasks[i][0],i,tasks[i][1]))
        x.sort()
        h=[]
        ans=[]
        i,t=0,x[0][0]
        while len(ans)<n:
            while i<n and t>=x[i][0]:
                heappush(h,(x[i][2],x[i][1]))
                i+=1
        
            if h:
                duration,ind=heappop(h)
                t+=duration
                ans.append(ind)
                
            elif i<n:
                t=x[i][0]
        
        return ans
            
            
            
        
        
        