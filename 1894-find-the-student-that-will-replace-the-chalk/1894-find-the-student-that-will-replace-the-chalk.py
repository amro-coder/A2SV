class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix_sum=[0]+list(accumulate(chalk))
        low,high,n=0,10**10,len(chalk)
        while low<=high:
            mid=((low+high)>>1)
            if (prefix_sum[-1]*(mid//n) + prefix_sum[mid%n])<=k:
                low=mid+1
            else:
                high=mid-1
        return n-1 if low%n==0 else low%n-1