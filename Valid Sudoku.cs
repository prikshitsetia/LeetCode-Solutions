public class Solution {
    public bool IsValidSudoku(char[][] board) {
        Dictionary<char,int> []row = new Dictionary<char,int>[9];
        Dictionary<char,int> []col = new Dictionary<char,int>[9];
        Dictionary<char,int> [] boxes= new Dictionary<char,int>[9];
        for(int i=0;i<9;i++)
        {
            row[i]=new Dictionary<char,int>();
            col[i]=new Dictionary<char,int>();
            boxes[i]=new Dictionary<char,int>();
        }
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if(board[i][j]!='.')
                {
                    if(row[i].ContainsKey(board[i][j]))
                        return false;
                    else
                        row[i].Add(board[i][j],1);
                    
                    if(col[j].ContainsKey(board[i][j]))
                    {
                        return false;
                    }
                    else{
                        col[j].Add(board[i][j],1);
                    }
                }   
                int boxindex=(i/3)*3+j/3;
                
                if(board[i][j]!='.')
                {
                    if(boxes[boxindex].ContainsKey(board[i][j]))
                    {
                        return false;
                    }
                    boxes[boxindex].Add(board[i][j],1);
                }
            }   
        }
        return true;
    }
}