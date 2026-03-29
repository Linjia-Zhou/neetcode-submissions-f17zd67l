# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head

        # find midpoint
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            t = second.next
            second.next = prev
            prev = second
            second = t

        # merge lists together
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2




    
              
