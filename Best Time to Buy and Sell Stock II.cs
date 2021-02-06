public class Solution {
    public int MaxProfit(int[] prices) {
        int valley=Int32.MaxValue;
        int profit=0;
        bool buy=false;
        for(int i=0;i<prices.Length;i++){
            if(buy &&i+1<prices.Length&& prices[i+1]<prices[i])
            {
                profit+=(prices[i]-valley);
                buy=false;
            }
            else if(buy && i==prices.Length-1 && prices[i]>valley){
                profit+=(prices[i]-valley);
            }
            else if(!buy &&i+1<prices.Length && prices[i+1]<prices[i]){
                continue;
            }
            else if(!buy &&i+1<prices.Length&& prices[i+1]>prices[i]){
                valley=prices[i];
                buy=true;
            }
        }
        return profit;
        
    }
}