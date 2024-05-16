# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1 :
            root1=TreeNode(0)
        if not root2:
            root2=TreeNode(0)
        
        def merge(r1,r2):
            r1.val+=r2.val
            if r1.left or r2.left:
                if not r1.left and r2.left:
                    r1.left=TreeNode(0)
                if not r2.left and r1.left:
                    r2.left=TreeNode(0)
                merge(r1.left,r2.left)
            
            if not r1.right and not r2.right:
                return
            if not r1.right and r2.right:
                r1.right=TreeNode(0)
            if not r2.right and r1.right:
                r2.right=TreeNode(0)
            merge(r1.right,r2.right)
        
        merge(root1,root2)
        return root1
            
            