class Solution
{
public:
    long long int coinChange(vector<int> &coins, int amount)
    {
        int dp[amount + 1];
        for (int i = 0; i <= amount; i++)
            dp[i] = amount + 1;
        dp[0] = 0;
        for (int i = 1; i <= amount; i++)
        {
            for (int coin : coins)
            {
                if (i - coin >= 0)
                {
                    int res = dp[i - coin] + 1;
                    dp[i] = min(dp[i], res);
                }
            }
        }
        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }
};