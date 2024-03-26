class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=[0]
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        cnt,ans=defaultdict(int),0
        for i in range(len(nums),-1,-1):
            ans+=cnt[prefix_sum[i]+k]
            cnt[prefix_sum[i]]+=1
        return ans
                
        