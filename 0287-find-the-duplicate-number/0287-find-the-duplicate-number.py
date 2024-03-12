class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low,high=1,len(nums)-1
        while low<=high:
            mid=(low+high)>>1
            if sum([i<=mid for i in nums])<=mid:
                low=mid+1
            else:
                high=mid-1
        return low
        