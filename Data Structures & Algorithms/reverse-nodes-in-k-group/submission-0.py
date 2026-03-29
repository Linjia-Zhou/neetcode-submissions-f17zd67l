# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        p, c, tail = None, head, head

        while c:
            t = c.next
            c.next = p
            p = c
            c = t

        return p, tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        chead = head # current head
        nhead = head # next head
        ptail, tail = head, head # previous tail, current tail
        i = 1

        while tail: # MIGHT NEED TO CHANGE
            if i % k == 0:
                nhead = tail.next
                tail.next = None # breaking connection
                chead, tail = self.reverse(chead)
                tail.next = nhead

                if i == k: # this is the first one, so need to remember head is here
                    head = chead 
                else:
                    ptail.next = chead
                    ptail = tail
                    
                tail = nhead
                chead = nhead
            else:
                tail = tail.next
            i += 1

        return head

            
