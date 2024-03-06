class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right=0,len(people)-1
        ans=0
        while left<=right:
            if left==right:
                ans+=1
                break
            if people[left]+people[right]<=limit:
                left+=1
                right-=1
            else:
                right-=1
            ans+=1
        return ans
                