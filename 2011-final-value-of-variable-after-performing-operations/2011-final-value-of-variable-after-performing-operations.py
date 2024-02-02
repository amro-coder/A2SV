class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        ans+=operations.count("++X")
        ans+=operations.count("X++")
        ans-=operations.count("--X")
        ans-=operations.count("X--")
        return ans
        
        