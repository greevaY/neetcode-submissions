# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # take heads of both the linked lists
        # compare them
        # if one is smaller, add to stack -> shift the head a step ahead who was smaller, keep the larger one; one head exists other does not then add everything; if one is null then the actual value goes
        # continue till head exists for both

        curr1 = list1
        curr2 = list2


        dummy = ListNode(0)     # throwaway starting node
        tail = dummy

        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                tail = tail.next
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = tail.next
                curr2 = curr2.next

        if curr1 is None:
            tail.next = curr2

        if curr2 is None:
            tail.next = curr1

        dummy = dummy.next
        return dummy
