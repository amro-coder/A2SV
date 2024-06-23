class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans,cur=[],[]
        def backtrack():
            r=len(cur)
            if r==n:
                ans.append(['.'*cur[i]+'Q'+'.'*(n-cur[i]-1) for i in range(n)])
            for c in range(n):
                if not any([abs(i-r)==abs(cur[i]-c) or cur[i]==c for i in range(r)]):
                    cur.append(c)
                    backtrack()
                    cur.pop()
        backtrack()
        return ans
    
                        
                    
            
        