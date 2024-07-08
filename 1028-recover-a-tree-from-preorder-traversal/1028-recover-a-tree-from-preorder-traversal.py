# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        val,depth=[],[]
        current_depth=0
        i=0
        while i<len(traversal):
            if traversal[i]=='-':
                current_depth+=1
                i+=1
            else:
                num=[]
                while i<len(traversal) and traversal[i]!='-':
                    num.append(traversal[i])
                    i+=1
                val.append(int(''.join(num)))
                depth.append(current_depth)
                current_depth=0
                        
        def createTree(start,end):
            if start>end:
                return None
            if start==end:
                return TreeNode(val[start])
            leftStart,rightStart=start+1,end+1
            for i in range(start+2,end+1):
                if depth[i]==depth[start]+1:
                    rightStart=i
                    break
            return TreeNode(val[start],createTree(leftStart,rightStart-1),createTree(rightStart,end))
        
        return createTree(0,len(val)-1)
                
        