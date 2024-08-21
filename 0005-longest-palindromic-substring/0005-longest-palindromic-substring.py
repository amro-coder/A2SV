class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher_odd(s):
            n=len(s)
            dp=[0]*n
            l,r=0,0
            for i in range(n):
                if i<=r: dp[i]=min(r-i,dp[l+r-i])
                while i-dp[i]-1>=0 and i+dp[i]+1<n and s[i+dp[i]+1]==s[i-dp[i]-1]: dp[i]+=1
                if i+dp[i]>r:
                    r=i+dp[i]
                    l=i-dp[i]
            return dp

        def manacher_even(s):
            n=len(s)
            dp=[-1]*n
            l,r=-1,-1
            for i in range(1,n):
                if i<=r: dp[i]=min(r-i,dp[l+r-i+1])
                while i-dp[i]-2>=0 and i+dp[i]+1<n and s[i+dp[i]+1]==s[i-dp[i]-2]: dp[i]+=1
                if i+dp[i]>r:
                    r=i+dp[i]
                    l=i-dp[i]-1
            return dp
        
        ans=1
        mo=manacher_odd(s)
        me=manacher_even(s)
        for val in mo:
            ans=max(ans,2*val+1)
        for val in me:
            ans=max(ans,2*val+2)
        for i in range(len(s)):
            if 2*mo[i]+1==ans:
                return s[i-mo[i]:i+mo[i]+1]
        for i in range(len(s)):
            if 2*me[i]+2==ans:
                return s[i-me[i]-1:i+me[i]+1]
        