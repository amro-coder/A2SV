# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[[] for _ in range(3000)]
        def assign_pos(node,r,c):
            if not node: return
            ans[c].append((r,node.val))
            assign_pos(node.left,r+1,c-1)
            assign_pos(node.right,r+1,c+1)
        assign_pos(root,0,1000)
        for i in range(len(ans)):
            ans[i].sort()
        final_ans=[]
        for i in range(len(ans)):
            if ans[i]:
                final_ans.append([temp[1] for temp in ans[i]])
        return final_ans
            
        