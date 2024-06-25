# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans=0
        def dfs(node,parentEven=False,grandParentEven=False):
            nonlocal ans
            if grandParentEven:
                ans+=node.val
            if node.left:
                dfs(node.left,not (node.val&1),parentEven)
            if node.right:
                dfs(node.right,not (node.val&1),parentEven)
        dfs(root)
        return ans
        