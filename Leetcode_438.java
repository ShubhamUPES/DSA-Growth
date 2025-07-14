import java.util.*;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if (s.length() < p.length()) return result;
        
        int[] pCount = new int[26];  // Frequency of characters in p
        int[] sCount = new int[26];  // Frequency in current window of s
        
        // Initialize frequency for p
        for (char c : p.toCharArray()) {
            pCount[c - 'a']++;
        }
        
        int window = p.length();
        
        for (int i = 0; i < s.length(); i++) {
            sCount[s.charAt(i) - 'a']++;
            
            // Remove leftmost char when window exceeds
            if (i >= window) {
                sCount[s.charAt(i - window) - 'a']--;
            }
            
            // Compare arrays
            if (Arrays.equals(pCount, sCount)) {
                result.add(i - window + 1);
            }
        }
        
        return result;
    }
}
