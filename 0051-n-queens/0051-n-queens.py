class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        ans = []
        cur = []
        
        def backtrack():
            nonlocal n
            if len(cur) == n:
                temp = []
                for j in cur:
                    temp.append('.' * j + 'Q' + '.' * (n - j - 1))
                ans.append(temp.copy())
                return
            
            r = len(cur)
            for c in range(n):
                for i in range(len(cur)):
                    j = cur[i]
                    if c == j or abs(c - j) == (r - i):
                        break
                else:
                    cur.append(c)
                    backtrack()
                    cur.pop()
        
        backtrack()
        return ans
        
        
#         [1, 3, 0, 2]
#         ['.Q..', '...Q']
#         [1, 3, j]
        
#         i, j = 0, 3
#         x, y = 2, 1


# 0, 1
# 1, 2
# 2, 3

# 0, 3
# 1, 2