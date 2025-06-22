class Solution {
    public static int sumOfDigits(int n) {
        int sum = 0;

        while (n > 0) {
            sum += n % 10;  // add last digit
            n = n / 10;     // remove last digit
        }

        return sum;
    }
}
