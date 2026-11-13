# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # get the head, store it in an array
        # check if it already exists in the array
        # if yes, return true
        # if no, move on

        curr = head

        a = []
        while curr:
            x = curr

            for i in a:
                if x == i:
                    return True

            a.append(x)

            curr = curr.next
        return False
        