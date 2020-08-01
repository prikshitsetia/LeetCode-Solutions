class Solution
{
public:
    int lengthOfLIS(vector<int> &nums)
    {
        if (nums.size() == 0)
            return 0;
        vector<int> length(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++)
        {
            int maxval = length[i];
            for (int j = i - 1; j >= 0; j--)
            {
                if (nums[i] > nums[j])
                {
                    maxval = max(maxval, length[i] + length[j]);
                }
            }
            length[i] = maxval;
        }
        int maxv = length[0];
        for (int i = 1; i < nums.size(); i++)
        {
            maxv = max(maxv, length[i]);
        }
        return maxv;
    }
};