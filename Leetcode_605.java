public class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        int i = 0;
        int len = flowerbed.length;

        while (i < len) {
            if (flowerbed[i] == 0) {
                boolean emptyLeft = (i == 0 || flowerbed[i - 1] == 0);
                boolean emptyRight = (i == len - 1 || flowerbed[i + 1] == 0);

                if (emptyLeft && emptyRight) {
                    flowerbed[i] = 1; // plant a flower
                    count++;
                    if (count >= n) return true;
                    i += 2; // skip next plot to maintain no-adjacent rule
                } else {
                    i++;
                }
            } else {
                i++; // current plot has flower
            }
        }

        return count >= n;
    }
}
