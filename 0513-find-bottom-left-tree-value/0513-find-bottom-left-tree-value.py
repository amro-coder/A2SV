# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dpMax={}
        dpMax[None]=0
        def getMaxDepth(node):
            if node==None: return 0
            dpMax[node]=max(getMaxDepth(node.left),getMaxDepth(node.right))+1
            return dpMax[node]
        getMaxDepth(root)
        def solve(node):
            if dpMax[node]==1:
                return node
            if dpMax[node.left]>=dpMax[node.right]:
                return solve(node.left)
            return solve(node.right)
        return solve(root).val