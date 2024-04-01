class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cnt=[0]*(1003)
        for num,start,end in trips:
            cnt[start]+=num
            cnt[end]-=num
        return max(accumulate(cnt))<=capacity
        