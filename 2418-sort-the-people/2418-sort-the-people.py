class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        x=[(heights[i],names[i]) for i in range(n)]
        # bubble sort
        for i in range(n):
            for j in range(i,n):
                if x[i]<x[j]:
                    x[i],x[j]=x[j],x[i]
        return [i[1] for i in x]