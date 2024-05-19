# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_min(r):
            while r.left: r=r.left
            return r.val
        def delete(r,key):# takes the tree and the key. returns the tree after deleting key
            if not r: return None
            if key<r.val: r.left=delete(r.left,key)
            if key>r.val: r.right=delete(r.right,key)
            if key==r.val:
                if not r.left: return r.right
                if not r.right: return r.left
                r.val=get_min(r.right)
                r.right=delete(r.right,r.val)
            return r
        return delete(root,key)
            
            
            
            
        
                
            
            