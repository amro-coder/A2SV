class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_pos=[0]*32
        cnt_neg=[0]*32
        for val in nums:
            if val>=0:
                for i in range(32):
                    cnt_pos[i]+=(val>>i)&1
            else:
                for i in range(32):
                    cnt_neg[i]+=(abs(val)>>i)&1
        ans=0
        for i in range(32):
            if cnt_pos[i]%3:
                ans+=1<<i
        for i in range(32):
            if cnt_neg[i]%3:
                ans-=1<<i
        return ans
            
        