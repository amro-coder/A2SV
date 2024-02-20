class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people=[i for i in range(1,n+1)]
        pointer=0
        while(len(people)>1):
            pointer=(pointer+k-1)%len(people)
            people.pop(pointer)
            pointer%=len(people)
        return people[0]
        
        