class Solution {
public:
    vector<string> li;
    vector<string> generateParenthesis(int n) {
        helper(n,n,"");
        return(li);
    }
    void helper(int o,int c,string str)
    {
        if(o==0 and c==0)
        {
            li.push_back(str);
            return;
        }
        if(o==0)
        {
            helper(o,c-1,str+")");
        }
        else if(o<c)
        {
            helper(o-1,c,str+"(");
            helper(o,c-1,str+")");
        }
        else
        {
            helper(o-1,c,str+"(");
        }
    }
};