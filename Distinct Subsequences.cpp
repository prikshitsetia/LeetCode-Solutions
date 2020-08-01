class Solution
{
public:
    int numDistinct(string s1, string s2)
    {

        long long int lcsStorage[s1.length() + 1][s2.length() + 1];

        memset(lcsStorage, -1, sizeof(lcsStorage));

        lcsStorage[s1.length()][s2.length()] = 1;

        for (int i = 0; i < s2.length(); i++)
            lcsStorage[s1.length()][i] = 0;
        for (int i = 0; i < s1.length(); i++)
            lcsStorage[i][s2.length()] = 1;

        for (int row = s1.length() - 1; row >= 0; row--)
        {
            for (int col = s2.length() - 1; col >= 0; col--)
            {

                if (s1[row] == s2[col])
                {

                    lcsStorage[row][col] = lcsStorage[row + 1][col] + lcsStorage[row + 1][col + 1];
                }
                else
                {

                    lcsStorage[row][col] = lcsStorage[row + 1][col];
                }
                //cout<<lcsStorage[row][col]<<endl;
            }
        }
        return lcsStorage[0][0];
    }
};