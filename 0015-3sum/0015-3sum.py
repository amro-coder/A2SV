class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        pos=[]
        neg=[]
        zeors=0
        for value in nums:
            if value>0:
                pos.append(value)
            elif value<0:
                neg.append(value)
            else:
                zeors+=1
        hash_pos=set(pos)
        hash_neg=set(neg)
        
        ans=set()
        # taking 3 zeors
        if zeors>2:
            ans.add((0,0,0))
        
        # taking one zero and one postive and one negative
        if zeors>0:
            for value in hash_pos:
                if -value in hash_neg:
                    ans.add((-value,0,value))
        
        # taking 2 postives and 1 negative
        for i in range(len(pos)):
            for j in range(i+1,len(pos)):
                if -(pos[i]+pos[j]) in hash_neg:
                    ans.add((-(pos[i]+pos[j]),pos[i],pos[j]))
                
        # taking 2 negatives and one postive
        for i in range(len(neg)):
            for j in range(i+1,len(neg)):
                if -(neg[i]+neg[j]) in hash_pos:
                    ans.add((neg[i],neg[j],-(neg[i]+neg[j])))
        
        return ans
                
        
        