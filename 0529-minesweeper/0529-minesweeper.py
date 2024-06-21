class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n,m=len(board),len(board[0])
        def reveal(x,y):
            if board[x][y]=='M':
                board[x][y]='X'
                return
            child=[(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
            cnt=sum([0<=i<n and 0<=j<m and board[i][j]=='M' for i,j in child])
            if cnt>0:
                board[x][y]=str(cnt)
                return
            board[x][y]='B'
            for i,j in child:
                if 0<=i<n and 0<=j<m and board[i][j]=='E':
                    reveal(i,j)
        reveal(*click)
        return board
                
                
            