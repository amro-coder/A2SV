class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        h=[(0,i,'r') for i in range(n)]+[(*i,'m') for i in meetings]
        heapify(h)
        cnt=[0]*n
        left=len(meetings)
        m,r=deque(),[]
        while left:
            a,b,t=heappop(h)
            if t=='r':
                if m:
                    heappush(h,(a+m.popleft(),b,'r'))
                    cnt[b]+=1
                    left-=1
                else:
                    heappush(r,b)                    
            else:
                if r:
                    index=heappop(r)
                    heappush(h,(b,index,'r'))
                    cnt[index]+=1
                    left-=1
                else:
                    m.append(b-a)
        return -max([(cnt[i],-i) for i in range(n)])[1]
            
            
        