class Solution:
    def fib(self, n: int) -> int:
        self.ans=defaultdict(lambda :-1)
        def solve(n):
            if self.ans[n]==-1:
                if n<=1:
                    self.ans[n]=n
                else:
                    self.ans[n]=solve(n-1)+solve(n-2)
            return self.ans[n]
        return solve(n)
        