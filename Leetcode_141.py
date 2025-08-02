class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head  # Step 1: Both start at head

        while fast and fast.next:  # Step 2: Traverse as long as fast doesn't reach the end
            slow = slow.next        # Move slow by 1 step
            fast = fast.next.next   # Move fast by 2 steps

            if slow == fast:        # Step 3: If they meet, there is a cycle
                return True

        return False  # Step 4: fast reached the end → no cycle
