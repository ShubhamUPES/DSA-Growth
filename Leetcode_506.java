
class Solution {
    public String[] findRelativeRanks(int[] score) {
        int n = score.length;
        String[] result = new String[n];

        // Step 1: Pair score with original index
        int[][] scoreWithIndex = new int[n][2];
        for (int i = 0; i < n; i++) {
            scoreWithIndex[i][0] = score[i]; // score
            scoreWithIndex[i][1] = i;        // original index
        }

        // Step 2: Sort by score in descending order
        Arrays.sort(scoreWithIndex, (a, b) -> b[0] - a[0]);

        // Step 3: Assign ranks
        for (int rank = 0; rank < n; rank++) {
            int index = scoreWithIndex[rank][1];
            if (rank == 0) {
                result[index] = "Gold Medal";
            } else if (rank == 1) {
                result[index] = "Silver Medal";
            } else if (rank == 2) {
                result[index] = "Bronze Medal";
            } else {
                result[index] = String.valueOf(rank + 1);
            }
        }

        return result;
    }
}
