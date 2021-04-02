# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fast = head
        slow = head
        while fast.next:
            slow = slow.next
            if not fast.next.next:
                break
            fast = fast.next.next
        return slow
