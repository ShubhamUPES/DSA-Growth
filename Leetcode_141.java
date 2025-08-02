class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) return false;

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;           // Move slow by 1 step
            fast = fast.next.next;      // Move fast by 2 steps

            if (slow == fast) {
                return true;            // Cycle detected
            }
        }

        return false;  // Reached the end → no cycle
    }
}
