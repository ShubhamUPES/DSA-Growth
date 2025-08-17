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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null) return null;

        // Create a dummy node before head
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        // Move to the node just before 'left'
        ListNode leftPre = dummy;
        ListNode currNode = head;
        for (int i = 0; i < left - 1; i++) {
            leftPre = leftPre.next;
            currNode = currNode.next;
        }

        // Reverse the sublist
        ListNode subListHead = currNode;
        ListNode preNode = null;
        for (int i = 0; i <= right - left; i++) {
            ListNode nextNode = currNode.next;
            currNode.next = preNode;
            preNode = currNode;
            currNode = nextNode;
        }

        // Connect the parts
        leftPre.next = preNode;
        subListHead.next = currNode;

        return dummy.next;
    }
}
