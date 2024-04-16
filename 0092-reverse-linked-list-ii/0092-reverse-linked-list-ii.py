# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node=head
        beforeLeft=None
        for i in range(left-1):
            beforeLeft=node
            node=node.next
        leftNode=node
        
        prevNode=node
        node=node.next
        for i in range(right-left):
            nextNode=node.next
            node.next=prevNode
            prevNode=node
            node=nextNode
            
        rightNode=prevNode
        afterRight=node
            
        leftNode.next=afterRight
        if beforeLeft:
            beforeLeft.next=rightNode
        else:
            head=rightNode
        
        return head
        
            
        