class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = []

        while head:
            temp.append(head.val)
            head = head.next

        g = h = None

        while temp:
            if not g:
                g = h = ListNode(temp.pop())
                continue
            g.next = ListNode(temp.pop())
            g = g.next

        return h
