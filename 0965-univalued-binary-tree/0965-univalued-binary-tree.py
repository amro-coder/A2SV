# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            return dfs(node.left) and dfs(node.right) and (len(set([node.val,node.right.val if node.right else node.val,node.left.val if node.left else node.val]))==1)
        return dfs(root)
        