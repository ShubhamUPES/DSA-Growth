import java.util.*;

class Solution {
    public int[] searchRange(int[] nums, int target) {
        List<Integer> indices = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                indices.add(i);
            }
        }

        if (indices.isEmpty()) {
            return new int[]{-1, -1};
        } else {
            return new int[]{indices.get(0), indices.get(indices.size() - 1)};
        }
    }
}


'''class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = findLeft(nums, target);
        int right = findRight(nums, target);

        if (left <= right) {
            return new int[]{left, right};
        }
        return new int[]{-1, -1};
    }

    private int findLeft(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int result = nums.length; 

        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] >= target) {
                right = mid - 1;
                result = mid;
            } else {
                left = mid + 1;
            }
        }
        return result;
    }

    private int findRight(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int result = -1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] <= target) {
                left = mid + 1;
                result = mid;
            } else {
                right = mid - 1;
            }
        }
        return result;
    }
}
'''
