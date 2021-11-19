# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        c = head
        while c:
            if c.next:
                temp = c.next
                v = c.val
                c.val = temp.val
                temp.val = v
            else:
                return head
            c = c.next.next
                
        return head