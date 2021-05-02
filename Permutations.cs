public class Solution {
    public IList<IList<int>> helper(List<int> nums, IList<int> ans, IList<IList<int>> final, int point)
    {
        if (nums.Count==0)
        {
            List<int> temp=new List<int>();
            foreach(int a in ans)
                temp.Add(a);
            final.Add(temp);
            return final;
        }
        for (int i = 0; i < nums.Count; i++)
        {
            ans.Add(nums[i]);
            List<int> temo=new List<int>();
            for(int j=0;j<nums.Count;j++)
            {
                if(i!=j)
                {
                    temo.Add(nums[j]);
                }
            }
            helper(temo, ans, final, i + 1);
            ans.RemoveAt(ans.Count-1);
        }
        return final;
    }
    public IList<IList<int>> Permute(int[] nums)
    {
        IList<IList<int>> temp = new List<IList<int>>();
        IList<int> a = new List<int>();
        List<int> temo=new List<int>(nums);
        return helper(temo, a, temp, 0);
    }
}