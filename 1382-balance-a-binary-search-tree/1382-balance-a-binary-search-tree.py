# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        value=[]
        stack=[root]
        while stack:
            parent=stack.pop()
            value.append(parent.val)
            if parent.right:
                stack.append(parent.right)
            if parent.left:
                stack.append(parent.left)
        value.sort()
        def CreateBst(start,end):
            if end-start+1==1:
                return TreeNode(value[start])
            if end-start+1==2:
                return TreeNode(value[end],TreeNode(value[start]))
            mid=(start+end)>>1
            root=TreeNode(value[mid],CreateBst(start,mid-1),CreateBst(mid+1,end))
            return root
        return CreateBst(0,len(value)-1)
        
        