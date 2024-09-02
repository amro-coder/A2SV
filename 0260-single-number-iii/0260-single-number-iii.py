class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_val=0
        for val in nums:
            xor_val^=val
        least_bit=xor_val&(-xor_val)
        num1=num2=0
        for val in nums:
            if val & least_bit: num1^=val
            else: num2^=val
        return [num1,num2]
        