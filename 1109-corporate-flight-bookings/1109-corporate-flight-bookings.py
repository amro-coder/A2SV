class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        cnt=[0]*(n+1)
        for first,last,num in bookings:
            cnt[first-1]+=num
            cnt[last]-=num
        return list(accumulate(cnt))[:n]
            
        
        