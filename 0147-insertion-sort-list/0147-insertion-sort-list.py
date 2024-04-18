# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cheating=[]
        while head:
            cheating.append(head)
            head=head.next
        cheating.sort(key=lambda a:a.val)
        for i in range(len(cheating)-1):
            cheating[i].next=cheating[i+1]
        cheating[-1].next=None
        return cheating[0]
            
        