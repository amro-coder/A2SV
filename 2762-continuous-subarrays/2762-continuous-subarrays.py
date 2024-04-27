class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        start,ans,cnt=0,0,defaultdict(int)
        for i in range(len(nums)):
            cnt[nums[i]]+=1
            while max(cnt.keys())-min(cnt.keys())>2:
                cnt[nums[start]]-=1
                if cnt[nums[start]]==0:
                    del cnt[nums[start]]
                start+=1
            ans+=i-start+1
        return ans
            
                