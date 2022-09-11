# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):

        address_list = {}
        position = 0
        while head is not None:
            if (
                head in address_list
            ):  # use return for correct statements instead of creating a negation of a statement
                return head
            address_list[head] = position
            head = head.next
            position += 1


list1 = ListNode(6)
list1.next = ListNode(8)
list1.next.next = list1.next
# list1.next.next.next = ListNode(12)
# list1.next.next.next.next = ListNode(13)
print(list1)
