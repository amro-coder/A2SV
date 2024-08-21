class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(x):
            n=len(x)
            dp=[0]*(n+2)
            for i in range(n-1,-1,-1):
                dp[i]=max(dp[i+1],x[i]+dp[i+2])
            return dp[0]
        return max(solve(nums[1:]),nums[0]+solve(nums[2:-1]))
                
        