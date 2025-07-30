

class Solution {
    public int buyChoco(int[] prices, int money) {
        Arrays.sort(prices);  // Sort the prices in ascending order
        if (prices[0] + prices[1] <= money) {
            return money - (prices[0] + prices[1]);  // Buy two cheapest chocolates
        } else {
            return money;  // Not enough money, return full amount
        }
    }
}
