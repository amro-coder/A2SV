class Solution:
    def reorganizeString(self, s: str) -> str:
        x=sorted([[v,k] for k,v in Counter(s).items()])
        max_freq=x[-1][0]
        rest_freq=sum([i[0] for i in x[:-1]])
        if max_freq-rest_freq>1:
            return ""
        ans=[]
        while x:
            if not ans or ans[-1]!=x[-1][1]:
                ans.append(x[-1][1])
                if x[-1][0]==1:
                    x.pop()
                else:
                    x[-1][0]-=1
            else:
                ans.append(x[-2][1])
                if x[-2][0]==1:
                    temp=x.pop()
                    x.pop()
                    x.append(temp)
                else:
                    x[-2][0]-=1
            x.sort()
        return "".join(ans)
        
        