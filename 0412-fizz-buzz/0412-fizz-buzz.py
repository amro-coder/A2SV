class Solution:
    def fizzBuzz(self, n: int):
        ans=[]
        for value in range(1,n+1):
            if value%3==0 and value%5==0:
                ans.append("FizzBuzz")
            elif value%3==0:
                ans.append("Fizz")
            elif value%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(value))
        return ans
        