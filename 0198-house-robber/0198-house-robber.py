class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[nums[-1]]*n
        for i in range(n-2,-1,-1):
            ans[i]=max(ans[i+1],nums[i]+(0 if i+2>=n else ans[i+2]))
        return ans[0]
        