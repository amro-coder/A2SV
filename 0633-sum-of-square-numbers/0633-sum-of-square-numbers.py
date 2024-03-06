class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        while a*a<=c:
            if int((c-a*a)**0.5)**2==c-a*a:
                return True
            a+=1
        return False