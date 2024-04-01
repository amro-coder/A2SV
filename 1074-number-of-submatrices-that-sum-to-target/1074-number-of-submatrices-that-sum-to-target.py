class Solution:
    def get_rectangle_sum(self,row1,row2,col):
        a = self.prefix_sum[row2 + 1][col + 1]
        b = self.prefix_sum[row1][col + 1]
        return a - b

    def numSubmatrixSumTarget(self, x: List[List[int]], target: int) -> int:
        n,m=len(x),len(x[0])
        self.prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.prefix_sum[i + 1][j + 1] = (x[i][j] + self.prefix_sum[i + 1][j])
        for i in range(n):
            for j in range(m):
                self.prefix_sum[i + 1][j + 1] += self.prefix_sum[i][j + 1]

        ans = 0
        for row1 in range(n):
            for row2 in range(row1,n):
                row1_to_row2_prefix=[0]
                for k in range(m):
                    row1_to_row2_prefix.append(self.get_rectangle_sum(row1,row2,k))
                cnt=defaultdict(int)
                for i in range(m+1):
                    ans+=cnt[row1_to_row2_prefix[i]-target]
                    cnt[row1_to_row2_prefix[i]]+=1

        return ans

        