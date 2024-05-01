class Solution:
    def decodeString(self, s: str) -> str:
        def getString(start,end):
            if start>end:
                return ""
            # if all([i.isalpha() for i in s[start:end+1]]):
            #     return s[start:end+1]
            if not s[start].isnumeric():
                return s[start]+getString(start+1,end)
            num=""
            while s[start].isnumeric():
                num+=s[start]
                start+=1
            cnt=0
            index=-1
            for i in range(start,end+1):
                if s[i]=="[":
                    cnt+=1
                elif s[i]=="]":
                    cnt-=1
                if cnt==0:
                    index=i
                    break
            ans=getString(start+1,index-1)*int(num)
            return ans+getString(index+1,end)
        
        return getString(0,len(s)-1)