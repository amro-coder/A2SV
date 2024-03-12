class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low,high=1,len(nums)-1
        while low<=high:
            mid=(low+high)>>1
            cnt=0
            for i in nums:
                if i<=mid:
                    cnt+=1
            if cnt<=mid:
                low=mid+1
            else:
                high=mid-1
        return low
        