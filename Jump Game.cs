public class Solution {
    public bool helper(int[] nums,int i,int[] dp){
        if(i==nums.Length-1){
            dp[i]=1;
            return true;
        }
        else if(i>nums.Length-1){
            dp[i]=0;
            return false;
        }
        if(dp[i]!=-1){
            if(dp[i]==1){
                return true;
            }
            return false;
        }
        for(int j=1;j<=nums[i];j++){
            if(helper(nums,i+j,dp)){
                dp[i+j]=1;
                return true;
            }
            dp[i+j]=0;
        }
        dp[i]=0;
        return false;
    }
    public bool CanJump(int[] nums) {
        int[] dp=new int[nums.Length];
        for(int i=0;i<nums.Length;i++){
            dp[i]=-1;
        }
        return helper(nums,0,dp);
        
    }
}