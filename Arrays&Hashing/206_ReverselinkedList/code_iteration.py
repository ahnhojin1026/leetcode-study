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

        prev = None
        cur = head
        # iterate through the linked list change the direction of the pointer
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev