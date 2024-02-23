class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n,m=len(mat),len(mat[0])
        ans=[]
        start=[(i,0) for i in range(n)] + [(n-1,i) for i in range(1,m)]
        for i in range(len(start)):
            current_diagonal=[]
            x,y=start[i]
            while x>=0 and y<m:
                current_diagonal.append(mat[x][y])
                x-=1
                y+=1
            if i&1:
                current_diagonal.reverse()
            ans.extend(current_diagonal)
        return ans
        