class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        s=""
        for i in range(n):
            s=s+"."
        li=[]
        board=[ s for j in range(n)]
        def canPlace(board,i,j):
            for k in range(n):
                if board[k][j]=="Q":
                    return False
                if board[i][k]=="Q":
                    return False
                if i+k<n and j-k>=0 and board[i+k][j-k]=="Q":
                    return False
                if i-k>=0 and j+k<n and board[i-k][j+k]=="Q":
                    return False
                if i-k>=0 and j-k>=0 and board[i-k][j-k]=="Q":
                    return False
                if i+k<n and j+k<n and board[i+k][j+k]=="Q":
                    return False
            return True
        def helper(board,i):
            if i==n:
                temp=[board[k] for k in range(n)]
                li.append(temp)
                return
            #ans=False
            for k in range(n):
                if canPlace(board,i,k):
                    board[i]=board[i][:k]+"Q"+board[i][k+1:]
                    #ans=
                    helper(board,i+1)
                    #if ans==False:
                    board[i]=board[i][:k]+"."+board[i][k+1:]
            return #ans
        helper(board,0)
        return li