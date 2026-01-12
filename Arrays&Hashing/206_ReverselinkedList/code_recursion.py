# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case []
        if not head or not head.next:
            return head
        # 1. deep dive to the end of the linked list
        new_head = self.reverseList(head.next)
        # 2. reverse the pointer direction
        # 2.1 make the next node point to the current node
        head.next.next = head
        # 2.2 cut off the original next pointer to avoid cycle
        head.next = None
        
        return new_head