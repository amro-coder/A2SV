class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        cnt=[0]*n
        j,cnt_unique,ans=0,0,0
        for i in range(n):
            while j<n and cnt_unique + (cnt[fruits[j]]==0) <3:
                cnt_unique+=(cnt[fruits[j]]==0)
                cnt[fruits[j]]+=1
                j+=1
            ans=max(ans,j-i)
            cnt_unique-=(cnt[fruits[i]]==1)
            cnt[fruits[i]]-=1
        return ans
                
                
        