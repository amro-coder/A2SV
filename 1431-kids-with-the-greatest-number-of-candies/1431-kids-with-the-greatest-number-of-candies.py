class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value=max(candies)
        return [candies[i]+extraCandies>=max_value for i in range(len(candies))]
        