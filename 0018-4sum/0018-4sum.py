class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        cnt=Counter(nums)
        ans=set()
        for i in range(n):
            cnt[nums[i]]-=1
            for j in range(i+1,n):
                cnt[nums[j]]-=1
                for k in range(j+1,n):
                    cnt[nums[k]]-=1
                    if cnt[target-nums[i]-nums[j]-nums[k]]>0:
                        temp=[target-nums[i]-nums[j]-nums[k],nums[i],nums[j],nums[k]]
                        ans.add(tuple(sorted(temp)))
                    cnt[nums[k]]+=1
                cnt[nums[j]]+=1
            cnt[nums[i]]+=1
        return list(ans)
                    
                    