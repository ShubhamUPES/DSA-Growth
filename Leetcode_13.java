class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> roman = Map.of(
            'I', 1, 'V', 5, 'X', 10,
            'L', 50, 'C', 100, 'D', 500, 'M', 1000
        );
        
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            int val = roman.get(s.charAt(i));
            if (i < s.length() - 1 && val < roman.get(s.charAt(i + 1))) {
                total -= val;
            } else {
                total += val;
            }
        }
        return total;
    }
}
