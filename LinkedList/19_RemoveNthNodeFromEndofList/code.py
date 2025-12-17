# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # exception case
        if head is None:
            return None
        
        # two-pointer method
        slow_prev = None
        slow = head
        fast = head

        # fast has to be n step further
        for i in range(n):
            fast = fast.next

        # iterate until fast reaches the end
        while fast:
            # update pointers
            fast = fast.next
            slow_prev = slow
            slow = slow.next
        
        # if slow_prev is None, it means we need to remove the head node
        if slow_prev is None:
            return head.next
        # if slow is not None, we need to remove the slow node
        elif slow:
            slow_prev.next = slow.next
        # if slow is None, it means we need to remove the last node
        else:
            slow_prev.next = None

        return head

        