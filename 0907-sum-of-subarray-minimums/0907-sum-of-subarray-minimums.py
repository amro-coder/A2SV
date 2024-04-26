class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod=10**9 + 7
        n=len(arr)        
        previousSmaller=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[i]<arr[stack[-1]]:
                previousSmaller[stack.pop()]=i
            stack.append(i)
            
        dp=[0]*(n+1)
        dp[0]=arr[0]
        for i in range(1,n):
            dp[i]=dp[previousSmaller[i]]+(i-previousSmaller[i])*arr[i]
        return sum(dp)%mod
        