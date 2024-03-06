class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=j=0
        ans=[]
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                ans.append(nums1[i])
                i+=1
            else:
                ans.append(nums2[j])
                j+=1
        ans.extend(nums1[i:m])
        ans.extend(nums2[j:n])
        for i in range(n+m):
            nums1[i]=ans[i]
                
        """
        Do not return anything, modify nums1 in-place instead.
        """
        