# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = '', ''

        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next

        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next
        
        s3 = str(int(s1) + int(s2))[::-1]
        head = ListNode()
        head.val = int(s3[0])
        curr = head

        for i in range(1, len(s3)):
            t = ListNode()
            t.val = int(s3[i])
            # curr.val = int(s3[i])
            curr.next = t
            curr = curr.next
        
        return head


        