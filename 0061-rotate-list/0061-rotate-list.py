# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        node=head
        tail=node
        while node:
            length+=1
            tail=node
            node=node.next
        if length==0:
            return None
        k%=length
        for i in range(length-k):
            tail.next=head
            tail=head
            head.next,head=None,head.next
        return head
        