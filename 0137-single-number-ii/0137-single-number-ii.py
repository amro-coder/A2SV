class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones=twos=0
        for val in nums:
            ones=(ones^val) & ~twos
            twos=(twos^val) & ~ones
        return ones