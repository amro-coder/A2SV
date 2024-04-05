class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        s=sum(nums)
        ans=target//s *len(nums)
        target%=s
        nums+=nums
        prefix_nums=[0]+list(accumulate(nums))
        last_index=defaultdict(lambda :-1)
        last_index[0]=0
        inc=float("inf")
        for i in range(len(nums)+1):
            if last_index[prefix_nums[i]-target]!=-1:
                inc=min(inc,i-last_index[prefix_nums[i]-target])
            last_index[prefix_nums[i]]=i
        return inc+ans if inc!=float("inf") else -1
    
        