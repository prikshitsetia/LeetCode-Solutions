class Solution
{
public:
    int numSquares(int n)
    {
        int dp[n + 1];
        memset(dp, -1, sizeof(dp));
        return perfectSquare(n, dp);
    }

    int perfectSquare(int n, int dp[])
    {
        dp[0] = 0;
        dp[1] = 1;
        if (n <= 0)
        {
            return 0;
        }

        if (dp[n] != -1)
            return dp[n];

        int minValue = INT_MAX;

        int square = 1;

        for (int i = 1; square <= n; i++)
        {
            minValue = min(minValue, perfectSquare(n - square, dp) + 1);
            dp[n] = minValue;
            square = i * i;
        }
        return dp[n];
    }
};