class Solution {
    public boolean validPalindrome(String s) {
        int n = s.length();
        
        for (int i = 0; i < n / 2; i++) {
            if (s.charAt(i) != s.charAt(n - 1 - i)) {
                String a = s.substring(i + 1, n - i);       // skip left
                String b = s.substring(i, n - 1 - i);       // skip right
                
                return isPalindrome(a) || isPalindrome(b);
            }
        }
        
        System.out.println(true);
        return true;
    }

    private boolean isPalindrome(String str) {
        int left = 0, right = str.length() - 1;
        
        while (left < right) {
            if (str.charAt(left) != str.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;
    }
}
