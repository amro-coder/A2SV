class Solution:
    def climbStairs(self, n: int) -> int:
        one,two,three=1,1,0
        for i in range(n):
            three=one+two
            one,two=two,three
        return one
        