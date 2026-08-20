class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head
        while curr:
            next_node = curr.next
            # Start from beginning of sorted list
            prev = dummy
            # Find correct position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            # Insert curr
            curr.next = prev.next
            prev.next = curr
            # Move to next original node
            curr = next_node
        
        return dummy.next
