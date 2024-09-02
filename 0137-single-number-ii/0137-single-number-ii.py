class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt=[0]*33
        for val in nums:
            for i in range(33):
                cnt[i]+=(val>>i)&1
        ans=0
        if cnt[32]%3==1:
            for i in range(33):
                if cnt[i]%3==0:
                    ans-=1<<i
            ans-=1
        else:
            for i in range(33):
                if cnt[i]%3:
                    ans+=1<<i
        return ans