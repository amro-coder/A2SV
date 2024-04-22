class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            if s[i]=='*':
                if ans:
                    ans.pop()
            else:
                ans.append(s[i])
        return ''.join(ans)
            
        