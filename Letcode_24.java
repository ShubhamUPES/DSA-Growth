/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        // Dummy node to handle edge cases cleanly
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        // Loop as long as there are at least two nodes to swap
        while (head != null && head.next != null) {
            ListNode first = head;       // first node
            ListNode second = head.next; // second node

            // Swap process
            prev.next = second;        // prev -> second
            first.next = second.next;  // first -> node after second
            second.next = first;       // second -> first

            // Move pointers forward for next swap
            prev = first;
            head = first.next;
        }

        return dummy.next;
    }
}
