public class Solution {
    public int countPrimes(int n) {
        if (n <= 2) return 0;

        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true); // Assume all numbers < n are prime
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false; // Mark all multiples of i as not prime
                }
            }
        }

        int primeCount = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) primeCount++;
        }

        return primeCount;
    }
}
