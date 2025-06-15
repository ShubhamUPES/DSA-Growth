
class Solution {
    public int findSubString(String s) {
        int n = s.length();
        Set<Character> distinctChars = new HashSet<>();
        
        // Count distinct characters
        for (char c : s.toCharArray()) {
            distinctChars.add(c);
        }
        int required = distinctChars.size();

        Map<Character, Integer> freq = new HashMap<>();
        int start = 0, count = 0, minLen = n;

        for (int end = 0; end < n; end++) {
            char endChar = s.charAt(end);
            freq.put(endChar, freq.getOrDefault(endChar, 0) + 1);

            if (freq.get(endChar) == 1) {
                count++;
            }

            // Try to minimize the window
            while (count == required) {
                minLen = Math.min(minLen, end - start + 1);

                char startChar = s.charAt(start);
                freq.put(startChar, freq.get(startChar) - 1);
                if (freq.get(startChar) == 0) {
                    count--;
                }
                start++;
            }
        }

        return minLen;
    }
}
