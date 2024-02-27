class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort(key=lambda a:arr2.index(a) if a in arr2 else len(arr2)+a)
        return arr1
        