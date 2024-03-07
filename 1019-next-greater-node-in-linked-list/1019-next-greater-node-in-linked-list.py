# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack=[]
        ans=[]
        index=0
        while head!=None:
            while stack and stack[-1][0]<head.val:
                ans.append((stack.pop()[1],head.val))
            stack.append((head.val,index))
            head=head.next
            index+=1
            
        while stack:
            ans.append((stack.pop()[1],0))
        
        final_ans=[0]*len(ans)
        for index,value in ans:
            final_ans[index]=value
            
        return final_ans