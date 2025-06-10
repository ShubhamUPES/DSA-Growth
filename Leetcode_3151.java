class Solution {
    public boolean isArraySpecial(List<Integer> nums) {
        boolean result = true;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums.get(i) % 2 == nums.get(i + 1) % 2) {
                result = false;
                break;
            }
        }
        return result;
    }
}
