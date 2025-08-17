# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None

        # Create a dummy node before head
        dummy = ListNode(0)
        dummy.next = head

        # Move to the node just before 'left'
        leftPre = dummy
        currNode = head
        for _ in range(left - 1):
            leftPre = leftPre.next
            currNode = currNode.next

        # Reverse the sublist
        subListHead = currNode
        preNode = None
        for _ in range(right - left + 1):
            nextNode = currNode.next
            currNode.next = preNode
            preNode = currNode
            currNode = nextNode

        # Connect the parts
        leftPre.next = preNode
        subListHead.next = currNode

        return dummy.next
