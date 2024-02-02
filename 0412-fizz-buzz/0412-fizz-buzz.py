class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for value in range(n):
            if (value+1)%3==0 and (value+1)%5==0:
                ans.append("FizzBuzz")
            elif (value+1)%3==0:
                ans.append("Fizz")
            elif (value+1)%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(value+1))
        return ans
        