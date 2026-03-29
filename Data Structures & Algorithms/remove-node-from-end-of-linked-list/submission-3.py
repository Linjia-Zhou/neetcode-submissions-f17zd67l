# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        p, c = None, head

        while c: 
            t = c.next
            c.next = p
            p = c
            c = t
        
        return p

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        rhead = self.reverse(head)
        p, c = None, rhead

        while count < n:
            p = c
            c = c.next
            count += 1

        if p is None:
            if c:
                return self.reverse(c.next)
            else:
                return

        p.next = c.next

        return self.reverse(rhead)



