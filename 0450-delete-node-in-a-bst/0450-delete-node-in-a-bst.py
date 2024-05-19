# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node,parent=root,None
        while node and node.val!=key:
            parent=node
            if key<node.val:
                node=node.left
            else:
                node=node.right
                
        if not node: return root

        if not node.left:
            if not parent: return node.right
            if parent.left==node: parent.left=node.right
            else: parent.right=node.right
            return root
        
        if not node.right:
            if not parent: return node.left
            if parent.left==node: parent.left=node.left
            else: parent.right=node.left
            return root
        
        parentReplace=None
        replaceNode=node.right
        while replaceNode.left:
            parentReplace=replaceNode
            replaceNode=replaceNode.left
        
        if parentReplace==None:
            replaceNode.left=node.left
            if not parent: return replaceNode
            if parent.left==node: parent.left=replaceNode
            else: parent.right=replaceNode
            return root            
        else:
            edgeReplaceNode=replaceNode
            while edgeReplaceNode.right:
                edgeReplaceNode=edgeReplaceNode.right
                
            edgeReplaceNode.right=node.right
            replaceNode.left=node.left
            parentReplace.left=None
            if not parent:
                return replaceNode
            if parent.left==node: parent.left=replaceNode
            else: parent.right=replaceNode
            return root
            
            
        
                
            
            