class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        right_bigger=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if (nums[i]<nums[right_bigger]):
                for j in range(len(nums)-1,i,-1):
                    if nums[j]>nums[i]:
                        nums[j],nums[i]=nums[i],nums[j]
                        break
                for j in range((len(nums)-i-1)//2):
                    nums[j+i+1],nums[~j]=nums[~j],nums[j+i+1]
                break
            right_bigger=i
        else:
            nums.reverse()