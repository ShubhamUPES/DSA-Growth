class Solution {
    public int largestAltitude(int[] gain) {
        int[] altitude = new int[gain.length + 1];
        altitude[0] = 0;

        for (int i = 0; i < gain.length; i++) {
            altitude[i + 1] = altitude[i] + gain[i];
        }

        int max = altitude[0];
        for (int alt : altitude) {
            if (alt > max) {
                max = alt;
            }
        }

        return max;
    }
}
