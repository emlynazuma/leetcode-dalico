# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentry = ListNode(-101)
        sentry.next = head

        last = sentry
        curr = sentry.next
        while curr:
            if curr.val != last.val:
                last = curr
            else:
                last.next = curr.next
            curr = curr.next
        return sentry.next
