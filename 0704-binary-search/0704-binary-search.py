class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index=bisect_left(nums,target)
        if index==len(nums) or nums[index]!=target:
            return -1
        return index
        