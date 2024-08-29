class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)
        rep=[0]*n
        for i in range(n):
            val=0
            for c in range(26):
                if chr(c+97) in words[i]:
                    val+=1<<c
            rep[i]=val
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if rep[i]&rep[j]==0:
                       ans=max(ans,len(words[i])*len(words[j]))
        return ans
                
        