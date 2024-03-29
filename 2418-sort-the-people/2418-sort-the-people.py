class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        x=[(heights[i],names[i]) for i in range(n)]
        
        # bubble sort
        for i in range(n):
            for j in range(i,n):
                if x[i]<x[j]:
                    x[i],x[j]=x[j],x[i]
                    
        # selection sort
        min_index=0
        for i in range(n):
            for j in range(min_index,n):
                if x[j]>x[min_index]:
                    x[j],x[min_index]=x[min_index],x[j]
            min_index+=1
            
        # insertion sort
        for last_sorted_index in range(n-1):
            index=last_sorted_index+1
            while index>0 and x[index]>x[index-1]:
                x[index],x[index-1]=x[index-1],x[index]
                index-=1
                
        # count sort
        max_height=100001
        sorted_list=[[] for _ in range(max_height)]
        for i in range(n):
            sorted_list[heights[i]].append(names[i])
        ans=[]
        for i in range(max_height-1,-1,-1):
            ans.extend(sorted_list[i])
        return ans
    
        return [i[1] for i in x]