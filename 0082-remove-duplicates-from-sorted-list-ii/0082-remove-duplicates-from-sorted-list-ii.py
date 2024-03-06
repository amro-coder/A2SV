# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node,ans_head=None,None
        node=head
        while node!=None:
            value,cnt=node.val,0
            node_copy=node
            while node!=None and node.val==value:
                cnt+=1
                node=node.next
            if cnt==1:
                if ans_head==None:
                    ans_head=prev_node=node_copy
                else:
                    prev_node.next=node_copy
                    prev_node=node_copy
                prev_node.next=None
        return ans_head
                
            
        