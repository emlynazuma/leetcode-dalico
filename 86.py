# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        be_head = be = ListNode(-101)
        af_head = af = ListNode(-101)
        curr = head
        while curr:
            if curr.val < x:
                be.next = curr
                be = be.next
            else:
                af.next = curr
                af = af.next
            curr = curr.next
        af.next = None
        be.next = af_head.next
        return be_head.next
