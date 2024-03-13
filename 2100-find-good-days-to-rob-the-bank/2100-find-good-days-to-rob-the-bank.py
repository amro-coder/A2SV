class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        left,right=[0]*len(security),[0]*len(security)
        for i in range(1,len(security)):
            if security[i]<=security[i-1]:
                left[i]=left[i-1]+1
        for i in range(len(security)-2,-1,-1):
            if security[i]<=security[i+1]:
                right[i]=right[i+1]+1
        return [i for i in range(len(security)) if left[i]>=time and right[i]>=time]
    
        