# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([(root,0)])
        ans=[]
        while q:
            parent,parentLevel=q.popleft()
            if parentLevel==len(ans):
                ans.append([])
            ans[parentLevel].append(parent.val)
            if parent.left:
                q.append((parent.left,parentLevel+1))
            if parent.right:
                q.append((parent.right,parentLevel+1))
        return ans
                
        