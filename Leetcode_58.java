class Solution {
    public int lengthOfLastWord(String s) {
        String[] words = s.trim().split("\\s+");  // Trim and split on whitespace
        return words[words.length - 1].length();
    }
}
