public class Solution {
    public int countSeniors(String[] details) {
        int count = 0;
        for (int i = 0; i < details.length; i++) {
            char[] temp = details[i].toCharArray(); // convert string to char array
            int age = Integer.parseInt("" + temp[11] + temp[12]); // combine chars and parse int
            if (age >= 60) {
                count++;
            }
        }
        return count;
    }
