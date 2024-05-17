# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_level=[-1]*(3001)
        min_level=[float("inf")]*(3001)
        def dfs(r,i=1):
            if not r: return
            level=int(log2(i))
            max_level[level]=max(max_level[level],i)
            min_level[level]=min(min_level[level],i)
            dfs(r.left,2*i)
            dfs(r.right,2*i+1)
        dfs(root)
        ans=1
        for i in range(3001):
            if max_level[i]!=-1 and min_level[i]!=float("inf"):
                ans=max(ans,max_level[i]-min_level[i]+1)
        return ans
 