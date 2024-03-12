class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # finding the cycle
        slow=nums[0]
        fast=nums[nums[0]]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[nums[fast]]
            
        # finding the start of the cycle, which is the answer
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
        