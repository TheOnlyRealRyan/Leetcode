# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This solution is innefecient O(n^2)
# Look up: Two-Pointer Technique (Slow and Fast Pointers with Head Start)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        cur_node = head
        memory = []
        while cur_node:
            memory.append(cur_node)
            if cur_node.next in memory:
                return True 
            cur_node = cur_node.next
        return False