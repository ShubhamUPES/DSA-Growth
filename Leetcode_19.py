class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = second = dummy
        
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move both until first reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Remove the nth node
        second.next = second.next.next
        
        return dummy.next
