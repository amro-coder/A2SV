class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(low,high,target):
            if low>high:
                return -1
            mid=(low+high)>>1
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                return binarySearch(mid+1,high,target)
            return binarySearch(low,mid-1,target)
        return binarySearch(0,len(nums)-1,target)
            
        