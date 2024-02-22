class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:           
        n=len(img)
        m=len(img[0])
        ans=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                sum_value=num=0
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if 0<=i+dx<n and 0<=j+dy<m:
                            num+=1
                            sum_value+=img[i+dx][j+dy]
                ans[i][j]=sum_value//num
        return ans