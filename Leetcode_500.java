class Solution {
    public List<String> findWords(String[] words) {
        String row1 = "qwertyuiop";
        String row2 = "asdfghjkl";
        String row3 = "zxcvbnm";
        
        List<String> result = new ArrayList<>();
        
        for (String word : words) {
            int[] rows = {0, 0, 0};
            String lowerWord = word.toLowerCase();
            
            for (char ch : lowerWord.toCharArray()) {
                if (row1.indexOf(ch) != -1) {
                    rows[0] = 1;
                } else if (row2.indexOf(ch) != -1) {
                    rows[1] = 1;
                } else if (row3.indexOf(ch) != -1) {
                    rows[2] = 1;
                }
            }

            if (rows[0] + rows[1] + rows[2] == 1) {
                result.add(word); // Add original case word
            }
        }
        
        return result;
    }
}
