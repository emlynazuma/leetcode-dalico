class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = []

        while l1 or l2:
            if (l1 and l2 and l2.val <= l1.val) or (l2 and not l1):
                res.append(l2.val)
                l2 = l2.next
            elif (l1 and l2 and l2.val > l1.val) or (l1 and not l2):
                res.append(l1.val)
                l1 = l1.next

        return list2node(res)


def list2node(res):
    res2 = last = None

    for item in res:
        if last:
            last.next = ListNode(item)
            last = last.next
            continue
        res2 = last = ListNode(item)
    return res2


if __name__ == "__main__":
    l1 = list2node([-9, 3])
    l2 = list2node([5, 7])
    print(l1)
    print(l2)
    solution = Solution()
    res = solution.mergeTwoLists(l1, l2)
    print(res)
