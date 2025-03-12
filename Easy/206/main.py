# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# I didnt fully complete this question, had the right idea to switch n and n+1 but implemented it poorly
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 09 - 
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev