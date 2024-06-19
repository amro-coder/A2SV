class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start,value,numParts):
            if start==len(s):
                return numParts>1
            ans=False
            for i in range(start,len(s)):
                if not ans and (value==float("inf") or int(s[start:i+1])==value):
                    ans|=backtrack(i+1,int(s[start:i+1])-1,numParts+1)
            return ans
        return backtrack(0,float("inf"),0)
                    
        