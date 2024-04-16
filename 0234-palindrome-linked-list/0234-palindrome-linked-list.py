# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x=[]
        node=head
        while node:
            x.append(node.val)
            node=node.next
        return x==x[::-1]
        