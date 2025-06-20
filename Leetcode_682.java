class Solution {
    public int calPoints(String[] operations) {
        List<Integer> b = new ArrayList<>();

        for (int i = 0; i < operations.length; i++) {
            String op = operations[i];

            if (op.equals("+")) {
                int sum = b.get(b.size() - 1) + b.get(b.size() - 2);
                b.add(sum);
            } else if (op.equals("D")) {
                b.add(2 * b.get(b.size() - 1));
            } else if (op.equals("C")) {
                b.remove(b.size() - 1);
            } else {
                b.add(Integer.parseInt(op));
            }
        }

        int total = 0;
        for (int num : b) {
            total += num;
        }

        return total;
    }
}
