# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Add a sentry before head.
        sentry = ListNode(-101)
        sentry.next = head

        last = sentry
        curr = sentry.next
        last_2nd = None
        dupl = False

        while curr:
            if last.val != curr.val:
                if dupl:
                    last_2nd.next = curr
                    dupl = False
                else:
                    last_2nd = last
                last = curr
            else:
                last.next = curr.next
                dupl = True
            curr = curr.next

        # Some clean up code when dupl is still true. it is just set last elem pointing to None
        if dupl:
            last_2nd.next = curr

        return sentry.next
