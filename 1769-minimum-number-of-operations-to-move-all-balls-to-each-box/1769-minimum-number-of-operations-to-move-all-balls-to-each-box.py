class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_indexes=[i for i in range(len(boxes)) if boxes[i]=='1']
        right_sum,left_sum,index_of_first_bigger_index=sum(one_indexes),0,0
        ans=[-1]*len(boxes)
        for i in range(len(boxes)):
            while index_of_first_bigger_index<len(one_indexes) and i>=one_indexes[index_of_first_bigger_index]:
                right_sum-=one_indexes[index_of_first_bigger_index]
                left_sum+= one_indexes[index_of_first_bigger_index]
                index_of_first_bigger_index+=1
            
            left_ans=index_of_first_bigger_index*i-left_sum
            right_ans=right_sum-(len(one_indexes)-index_of_first_bigger_index)*i
            ans[i]=left_ans+right_ans
        return ans
            
                
            
            
            
        