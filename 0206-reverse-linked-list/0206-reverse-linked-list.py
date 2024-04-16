# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node=head
        ans=[]
        while node:
            ans.append(node)
            node=node.next
        ans.reverse()
        for i in range(len(ans)-1):
            ans[i].next=ans[i+1]
        ans[-1].next=None
        return ans[0]
            
        