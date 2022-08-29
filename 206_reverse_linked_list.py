# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):

        if head.next is None:
            return []

        # tmp = head
        ahead = head.next
        # prev_node = ListNode(-1)

        last_node = None

        while ahead is not None:
            head.next = last_node
            last_node = head
            head = ahead
            ahead = ahead.next

        head.next = last_node
        # head.next = None
        # last_node.next = None
        last_node = head
        return head


list1 = ListNode(6)
list1.next = ListNode(8)
list1.next.next = ListNode(11)
# list1.next.next.next = ListNode(13)
# list1.next.next.next.next = ListNode(17)

obj = Solution()
reverse_list = obj.reverseList(list1)
reverse_list
