class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        current_sum=1
        for i in range(len(digits)-1,-1,-1):
            current_sum+=digits[i]
            digits[i]=current_sum%10
            current_sum//=10
        if current_sum>0:
            digits.insert(0,current_sum)
        return digits
            
        