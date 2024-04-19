"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        ansHead=Node(head.val)
        lastNode=ansHead
        node=head.next
        while node:
            currentNode=Node(node.val)
            lastNode.next=currentNode
            lastNode=lastNode.next
            node=node.next
        lastNode.next=None
        
        node1=ansHead
        node2=head
        while node1:
            if node2.random:
                temp_node1=ansHead
                temp_node2=head
                while temp_node2!=node2.random:
                    temp_node1=temp_node1.next
                    temp_node2=temp_node2.next
                node1.random=temp_node1
            else:
                node1.random=None
            node1=node1.next
            node2=node2.next
        
        
        
        return ansHead
        
        