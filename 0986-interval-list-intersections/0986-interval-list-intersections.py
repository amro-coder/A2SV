class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans,j=[],0
        for i in range(len(firstList)):
            while j<len(secondList) and secondList[j][0]<=firstList[i][1]:
                if not(firstList[i][1]<secondList[j][0] or firstList[i][0]>secondList[j][1]):
                    ans.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
                j+=1
            j=max(j-1,0)
        return ans
                
                
            
        