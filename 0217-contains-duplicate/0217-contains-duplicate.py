class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x=set()
        for value in nums:
            if value in x:
                return True
            x.add(value)
        return False
    
        