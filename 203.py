# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        last = sentry = ListNode(-1)
        curr = sentry.next = head

        while curr:
            if curr.val == val:
                last.next = curr.next
            else:
                last = last.next
            curr = curr.next

        return sentry.next
