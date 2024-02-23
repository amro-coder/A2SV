class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n,m=len(strs),len(strs[0])
        ans=0
        for j in range(m):
            current_col=[]
            for i in range(n):
                current_col.append(strs[i][j])
            ans+=current_col!=sorted(current_col)
        return ans
            