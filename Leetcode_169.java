

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> freq = new HashMap<>();
        int n = nums.length / 2;

        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            if (freq.get(num) > n) return num;
        }

        return -1; // Just in case, though problem guarantees a majority
    }
}
