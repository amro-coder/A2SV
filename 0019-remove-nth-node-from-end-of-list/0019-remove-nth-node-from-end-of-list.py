# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        beforeNode=ListNode()
        beforeNode.next=head
        endNode=head
        for i in range(n-1):
            endNode=endNode.next
        while endNode.next:
            beforeNode=beforeNode.next
            endNode=endNode.next
            
        if beforeNode.next==head:
            return head.next
        beforeNode.next=beforeNode.next.next
        return head
            
        
        