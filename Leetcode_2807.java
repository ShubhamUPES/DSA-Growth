// LeetCode provides the ListNode class.
class Solution {
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        ListNode curr = head;

        while (curr != null && curr.next != null) {
            int g = gcd(curr.val, curr.next.val);

            ListNode node = new ListNode(g); // new node holds the gcd
            node.next = curr.next;           // link new node to the next original node
            curr.next = node;                // link current node to the new node

            curr = node.next;                // move to next original node (skip inserted)
        }
        return head;
    }

    private int gcd(int a, int b) {
        // Euclid's algorithm (iterative is also fine)
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}
