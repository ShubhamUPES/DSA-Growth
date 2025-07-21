class Solution {
    public int countSubstrings(String s) {
        int n = s.length();
        int count = 0;

        // Generate all substrings
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                String sub = s.substring(i, j + 1);
                if (isPalindrome(sub)) {
                    count++;
                }
            }
        }

        return count;
    }

    // Helper method to check if a string is a palindrome
    private boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;  // Not a palindrome
            }
            left++;
            right--;
        }

        return true;
    }
}
