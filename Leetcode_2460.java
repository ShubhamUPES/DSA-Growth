import java.util.*;

class Solution {
    public int[] applyOperations(int[] nums) {
        // Step 1: Apply doubling rule
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }

        // Step 2: Move all 0s to the end (two-pointer approach)
        int[] result = new int[nums.length];
        int index = 0;

        for (int num : nums) {
            if (num != 0) {
                result[index++] = num;
            }
        }

        return result;
    }
}
