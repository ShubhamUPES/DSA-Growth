class Solution {
    public int maxProduct(int[] nums) {
        int maxProd = nums[0];
        int currMax = nums[0];
        int currMin = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            
            // If current number is negative, swap currMax and currMin
            if (num < 0) {
                int temp = currMax;
                currMax = currMin;
                currMin = temp;
            }
            
            currMax = Math.max(num, num * currMax);
            currMin = Math.min(num, num * currMin);
            
            maxProd = Math.max(maxProd, currMax);
        }
        
        return maxProd;
    }
}
