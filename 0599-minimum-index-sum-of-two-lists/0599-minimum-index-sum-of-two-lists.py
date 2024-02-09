class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_in_list1={}
        index_in_list2={}
        for i in range(len(list1)):
            if list1[i] not in index_in_list1:
                index_in_list1[list1[i]]=i
        for i in range(len(list2)):
            if list2[i] not in index_in_list2:
                index_in_list2[list2[i]]=i
        least_index_sum=float("inf")
        for key,value in index_in_list1.items():
            if (key in index_in_list2):
                least_index_sum=min(least_index_sum,value+index_in_list2[key])
        if least_index_sum==float("inf"):
            return []
        # else:
        ans=[]
        for key,value in index_in_list1.items():
            if (key in index_in_list2) and (value+index_in_list2[key])==least_index_sum:
                ans.append(key)
        return ans
        
                
            
            
        
        