import java.util.*;

class Solution {
    public int removeDuplicates(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer> expected = new ArrayList<>();

        for (int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
            if (count.get(num) <= 2) {
                expected.add(num);
            }
        }

        // Copy back to nums array to simulate in-place change
        for (int i = 0; i < expected.size(); i++) {
            nums[i] = expected.get(i);
        }

        return expected.size();
    }
}
