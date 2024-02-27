class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        min_index=arr.index(min(arr))
        arr[:min_index+1]=arr[min_index::-1]
        ans=[min_index+1]
        for i in range(1,len(arr)):
            right_index=bisect_right(arr[:i],arr[i])
            if right_index!=i:
                ans.extend([i+1,i-right_index+1,i-right_index,i+1])
                arr[:i+1]=sorted(arr[:i+1])
        return ans