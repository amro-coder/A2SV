class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(float("-inf"))
        mod,n,ans,stack=10**9 + 7,len(arr),0,[(float("-inf"),-1)]
        for i in range(n):
            while arr[i]<stack[-1][0]:
                val,mid=stack.pop()
                ans+=(mid-stack[-1][1])*(i-mid)*val
            stack.append((arr[i],i))
        return ans%mod
                
                
                
                