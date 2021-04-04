# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        i = 0
        fast = slow = head
        while i < k - 1:
            fast = fast.next
            i += 1

        forw = fast

        while fast.next:
            fast = fast.next
            slow = slow.next

        bakw = slow
        bakw.val, forw.val = forw.val, bakw.val

        return head
