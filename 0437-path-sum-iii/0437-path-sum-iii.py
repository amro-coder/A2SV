# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        num=0
        def dfs(node):
            nonlocal num
            if not node:
                return []
            ans=dfs(node.left)+dfs(node.right)
            for i in range(len(ans)):
                ans[i]+=node.val
            ans.append(node.val)
            num+=ans.count(targetSum)
            return ans
        dfs(root)
        return num