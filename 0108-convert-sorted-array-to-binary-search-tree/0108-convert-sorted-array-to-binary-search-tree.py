# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def constructTree(start,end):
            length=end-start+1
            if length==1:
                return TreeNode(nums[start])
            if length==2:
                return TreeNode(nums[end],constructTree(start,start))
            mid=(start+end)>>1
            root=TreeNode(nums[mid],constructTree(start,mid-1),constructTree(mid+1,end))
            return root
        return constructTree(0,len(nums)-1)