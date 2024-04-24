class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans=defaultdict(lambda:-1)
        for val in nums2:
            while stack and stack[-1]<val:
                ans[stack.pop()]=val
            stack.append(val)
        return [ans[val] for val in nums1]

                
        