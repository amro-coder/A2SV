class Solution:
    def get_rectangle_sum(self,row1,col1,row2,col2,n,m):
        row1,row2=max(row1,0),min(row2,n-1)
        col1,col2=max(col1,0),min(col2,m-1)
        a=self.prefix_sum[row2+1][col2+1]
        b=self.prefix_sum[row1][col2+1]
        c=self.prefix_sum[row2+1][col1]
        d=self.prefix_sum[row1][col1]
        return a-b-c+d
    
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        
        self.prefix_sum=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.prefix_sum[i+1][j+1]=(matrix[i][j]+self.prefix_sum[i+1][j])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.prefix_sum[i+1][j+1]+=self.prefix_sum[i][j+1]
        
        return [[self.get_rectangle_sum(i-k,j-k,i+k,j+k,len(matrix),len(matrix[0])) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
    
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)