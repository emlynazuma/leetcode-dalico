# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dum = ListNode(0)
        dum.next = head
        fast = slow = dum

        i = 0
        while i < n + 1:
            fast = fast.next
            i += 1

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dum.next
