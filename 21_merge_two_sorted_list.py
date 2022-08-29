# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeTwoLists(list1, list2):

        dummy_node = ListNode()
        prev_pointer = dummy_node

        while list1 is not None and list2 is not None:

            if list1.val <= list2.val:
                prev_pointer.next = list1
                list1 = list1.next
            else:
                prev_pointer.next = list2
                list2 = list2.next
            prev_pointer = prev_pointer.next

        prev_pointer.next = list1 or list2

        return dummy_node.next


list1 = ListNode(6)
list1.next = ListNode(8)
list1.next.next = ListNode(11)
list1.next.next.next = ListNode(13)
list1.next.next.next.next = ListNode(17)

list2 = ListNode(7)
list2.next = ListNode(9)
list2.next.next = ListNode(10)
list2.next.next.next = ListNode(23)
list2.next.next.next.next = ListNode(29)

Solution.mergeTwoLists(list1, list2)
