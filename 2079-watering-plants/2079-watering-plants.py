class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans=0
        water_in_can=capacity
        for i in range(len(plants)):
            if water_in_can<plants[i]:
                water_in_can=capacity
                ans+=2*i
            water_in_can-=plants[i]
            ans+=1
        return ans
            
        