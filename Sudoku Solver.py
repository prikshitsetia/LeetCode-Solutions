class Solution:
    def canPlace(self,board,i,j,num):
        for k in range(9):
            if board[k][j]==str(num) or board[i][k]==str(num):
                return False
        row=int(i/3)*3
        col=int(j/3)*3
        for k in range(row,row+3):
            for m in range(col,col+3):
                if board[k][m]==str(num):
                    return False
        return True
    
    def helper(self,board,i,j):
        if i>=9:
            return True
        if j>=9:
            return self.helper(board,i+1,0)
        if board[i][j]!=".":
            return self.helper(board,i,j+1)
        
        for k in range(1,10):
            if self.canPlace(board,i,j,k):
                board[i][j]=str(k)
                ans=self.helper(board,i,j+1)
                if ans:
                    return True
        board[i][j]="."
        return False
                
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board,0,0)