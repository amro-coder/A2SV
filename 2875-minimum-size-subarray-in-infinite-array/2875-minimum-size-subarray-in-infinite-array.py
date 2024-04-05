class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        ans=float("inf")
        extended_nums=nums+nums
        c=sum(nums)
        rem=target%c
        prefix_ex_nums=[0]+list(accumulate(extended_nums))
        last_index=defaultdict(lambda :-1)
        for i in range(len(extended_nums)+1):
            if last_index[(prefix_ex_nums[i]%c-rem)%c]!=-1:
                temp_sum=prefix_ex_nums[i]-prefix_ex_nums[last_index[(prefix_ex_nums[i]%c-rem)%c]]
                ans=min(ans,i-last_index[(prefix_ex_nums[i]%c-rem)%c] + ((target-temp_sum)//c)*len(nums))
            if last_index[prefix_ex_nums[i]%c]==-1 or prefix_ex_nums[i]>=prefix_ex_nums[last_index[prefix_ex_nums[i]%c]]:
                last_index[prefix_ex_nums[i]%c]=i
        
        return ans if ans!=float("inf") else -1
    
        