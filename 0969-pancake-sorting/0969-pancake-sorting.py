class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n,ans=len(arr),[]
        for i in range(n):
            max_index=arr[:n-i].index(max(arr[:n-i]))
            arr[:max_index+1]=arr[max_index::-1]
            arr[:n-i]=arr[n-1-i::-1]
            ans.extend([max_index+1,n-i])
        return ans