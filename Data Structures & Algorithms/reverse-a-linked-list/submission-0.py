# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        stack = []

        curr = head
        while curr:
            x = curr
            stack.append(x)
            curr = curr.next
        
        if not stack:
            return None
        
        new_head = stack.pop()
        y = new_head

        while stack:
            y.next = stack.pop()
            y = y.next
        
        y.next = None
        return new_head
        