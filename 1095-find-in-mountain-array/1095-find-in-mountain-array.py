# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        ask=mountain_arr.get
        low,high=0,n-1
        while low<=high:
            mid=(low+high)>>1
            if mid+1>=n or ask(mid)>ask(mid+1):
                high=mid-1
            else:
                low=mid+1
        mid_arr=low
        
        low,high=0,mid_arr
        while low<=high:
            mid=(low+high)>>1
            if ask(mid)<=target:
                low=mid+1
            else:
                high=mid-1
        if high>=0 and ask(high)==target:
            return high
        
        low,high=mid_arr,n-1
        while low<=high:
            mid=(low+high)>>1
            if ask(mid)>=target:
                low=mid+1
            else:
                high=mid-1
        if high>=0 and ask(high)==target:
            return high
        return -1
        
        
        