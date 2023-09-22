# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def calc_len(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        idx = calc_len(head) - n

        if idx == 0:
            return head.next

        counter = 0
        temp = head
        while temp:
            if counter == idx - 1:
                temp.next = temp.next.next
            counter += 1
            temp = temp.next

        return head
