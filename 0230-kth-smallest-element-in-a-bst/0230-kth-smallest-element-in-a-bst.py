# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size=1
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def get_size(node):
            if not node: return 0
            node.size=get_size(node.left)+get_size(node.right)+1
            return node.size
        
        get_size(root)
        
        def solve(r,i):
            left_size=r.left.size if r.left else 0
            right_size=r.right.size if r.right else 0
            if i<=left_size: return solve(r.left,i)
            elif i==left_size+1: return r.val
            return solve(r.right,i-left_size-1)   
        
        return solve(root,k) 