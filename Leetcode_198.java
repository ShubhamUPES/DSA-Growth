class Solution {
    public int rob(int[] nums) {
        int prev1 = 0; // dp[i-1]: max money till previous house
        int prev2 = 0; // dp[i-2]: max money till two houses back

        for (int num : nums) {
            int temp = prev1;
            prev1 = Math.max(prev1, prev2 + num); // max of skipping or robbing current house
            prev2 = temp; // move prev1 to prev2 for next iteration
        }

        return prev1;
    }
}
