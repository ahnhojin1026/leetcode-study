# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # use two pointers, one going slow and the other going fast
        slow = head
        fast = head
        
        # move until the end of the LinkedList
        while fast is not None and fast.next is not None:
            # slow pointer moves one step
            slow = slow.next
            # fast pointer moves two steps
            fast = fast.next.next
            # i.e they move at relative speed of one step
            # if there is a cycle, they will eventually meet
            if slow == fast:
                return True
        return False

        