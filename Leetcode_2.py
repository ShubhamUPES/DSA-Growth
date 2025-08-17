# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: extract digits from linked lists into arrays
        arr1, arr2 = [], []
        while l1:
            arr1.append(l1.val)
            l1 = l1.next
        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        # Step 2: reverse arrays
        arr1.reverse()
        arr2.reverse()

        # Step 3: convert to numbers
        num1 = int("".join(map(str, arr1)))
        num2 = int("".join(map(str, arr2)))

        # Step 4: add
        total = num1 + num2

        # Step 5: convert sum → reversed digits array
        arr_sum = [int(d) for d in str(total)][::-1]

        # Step 6: convert array → linked list
        dummy = ListNode()
        curr = dummy
        for d in arr_sum:
            curr.next = ListNode(d)
            curr = curr.next

        return dummy.next
