class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans=[]
        i=len(s)-1
        while(i>=0):
            if (s[i]=='#'):
                ans.append(chr(96+int(s[i-2:i])))
                i-=3
            else:
                ans.append(chr(96+int(s[i])))
                i-=1
        return ''.join(reversed(ans))
                
        