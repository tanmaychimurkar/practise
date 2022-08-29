# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):

        current = head

        length = 0
        while current is not None:
            length += 1
            current = current.next

        if length % 2 == 0:
            middle_elem = int((length - 1) / 2) + 1
        elif round(length / 2) % 2 == 0:
            middle_elem = int((length + 1) / 2) - 1

        index = 0
        current = head
        while index != middle_elem:
            current = current.next
            index += 1

        return current


list1 = ListNode(6)
list1.next = ListNode(8)
list1.next.next = ListNode(11)
list1.next.next.next = ListNode(12)
list1.next.next.next.next = ListNode(13)

obj = Solution()
value = obj.middleNode(list1)
print(value)
