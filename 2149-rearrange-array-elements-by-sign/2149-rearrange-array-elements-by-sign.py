class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for value in nums:
            if value>0:
                pos.append(value)
            else:
                neg.append(value)
        ans=[]
        for i in range(len(pos)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
        