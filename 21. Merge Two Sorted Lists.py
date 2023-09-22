# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy

        temp1, temp2 = list1, list2

        while temp1 and temp2:
            inserted_node = None
            if temp1.val <= temp2.val:
                inserted_node = temp1
                temp1 = temp1.next

            else:
                inserted_node = temp2
                temp2 = temp2.next

            dummy.next = inserted_node
            dummy.next.next = None
            dummy = dummy.next


        if temp1:
            dummy.next = temp1

        if temp2:
            dummy.next = temp2

        return res.next



