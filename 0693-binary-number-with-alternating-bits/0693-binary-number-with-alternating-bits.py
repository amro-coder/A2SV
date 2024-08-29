class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        ans=1
        for i in range(n.bit_length()-1):
            ans&=(n>>i)^(n>>(i+1))
        return ans
        