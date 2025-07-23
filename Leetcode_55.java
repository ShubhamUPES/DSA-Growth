class Solution {
    public boolean canJump(int[] nums) {
        int reachable = 0;  // Maximum index we can currently reach
        
        for (int i = 0; i < nums.length; i++) {
            if (i > reachable) {
                return false;  // If we can't reach this index, return false
            }
            reachable = Math.max(reachable, i + nums[i]);  // Update the farthest we can go
        }
        
        return true;  // If loop completes, last index is reachable
    }
}
