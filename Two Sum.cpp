#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> h;
        vector<int> arr;
        for (int i = 0; i < nums.size(); i++)
        {
            if (h.count(target - nums[i]))
            {
                arr.push_back(h[target - nums[i]]);
                arr.push_back(i);
                break;
            }
            h[nums[i]] = i;
        }
        return arr;
    }
};