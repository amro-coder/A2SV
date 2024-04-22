class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        cnt=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!="*" and cnt==0:
                ans.append(s[i])
            else:
                if s[i]=="*":
                    cnt+=1
                else:
                    cnt-=1
        return ''.join(reversed(ans))
            
        