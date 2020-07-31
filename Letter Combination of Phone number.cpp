class Solution {
public:
    string keycode[10] = {".","#","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    vector<string> li;
    void helper(string digits,string ans)
    {
        if (digits.length()==0)
        {
            li.push_back(ans);
            return;
        }
        char ch=digits[0];
        string ros=digits.substr(1);
        string key = keycode[ch - '0'];
        for(int i=0;i<key.length();i++)
        {
            helper(ros,ans+key[i]);
        }
    }
    vector<string> letterCombinations(string digits) {
        if (digits.length()==0)
        {
            return li;
        }
        helper(digits,"");
        return li;
    }
};