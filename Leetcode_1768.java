class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] a = word1.toCharArray();
        char[] b = word2.toCharArray();
        StringBuilder result = new StringBuilder();

        int minLen = Math.min(a.length, b.length);

        for (int i = 0; i < minLen; i++) {
            result.append(a[i]).append(b[i]);
        }
        if (a.length > minLen) {
            result.append(word1.substring(minLen));
        }

        if (b.length > minLen) {
            result.append(word2.substring(minLen));
        }

        return result.toString();
    }
}
