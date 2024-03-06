class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        for i in range((n-k)//2):
            nums[i],nums[n-k-1-i]=nums[n-k-1-i],nums[i]
        for i in range(k//2):
            nums[n-k+i],nums[~i]=nums[~i],nums[n-k+i]
        nums.reverse()
        
            
        
            
        