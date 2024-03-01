class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans=0
        cnt=sorted(Counter(nums).items(),reverse=True)
        current_cnt=0
        for i in range(len(cnt)-1):
            current_cnt+=cnt[i][1]
            ans+=current_cnt
        return ans
            
            
        