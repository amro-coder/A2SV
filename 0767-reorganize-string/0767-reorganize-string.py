class Solution:
    def reorganizeString(self, s: str) -> str:
        x=sorted([[v,k] for k,v in Counter(s).items()])
        max_freq=x[-1][0]
        rest_freq=sum([i[0] for i in x[:-1]])
        if max_freq-rest_freq>1:
            return ""
        ans=['']*(len(s))
        for i in range(0,len(s),2):
            ans[i]=x[-1][1]
            x[-1][0]-=1
            if x[-1][0]==0:
                x.pop()
        for i in range(1,len(s),2):
            ans[i]=x[-1][1]
            x[-1][0]-=1
            if x[-1][0]==0:
                x.pop()
            
        return "".join(ans)
        
        