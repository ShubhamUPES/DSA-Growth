import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0)
            return 0;

        // Remove duplicates
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        // Convert set to array and sort
        int[] uniqueNums = new int[set.size()];
        int index = 0;
        for (int num : set) {
            uniqueNums[index++] = num;
        }
        Arrays.sort(uniqueNums);

        int curLen = 1;
        int maxLen = 1;

        for (int i = 0; i < uniqueNums.length - 1; i++) {
            if (uniqueNums[i + 1] == uniqueNums[i] + 1) {
                curLen++;
                maxLen = Math.max(maxLen, curLen);
            } else {
                curLen = 1;
            }
        }

        return maxLen;
    }
}
