# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverselist(self, head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


def reverseList2(self, head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
