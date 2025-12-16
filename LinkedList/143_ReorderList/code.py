# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # error handleing
        if head is None:
            return None

        # Step 1 : find the middle use fast-slow pointer
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        
        # Step 2 : starting from the middle (slow.next) reverse the back part of the list
        prev_node = None
        cur_node = slow.next
        # seperate front part and back part
        slow.next = None

        # rever the back part
        while cur_node is not None:
            # store next node
            next_node = cur_node.next
            # reverse the link
            cur_node.next = prev_node
            # update pointers
            prev_node = cur_node
            cur_node = next_node
            
        # Step 3 : reorder list by merging two parts
        # When list length is 2n : front part(n+1), back part (n-1)
        # When list length is 2n+1 : front part(n+1), back part (n)
        front_part = head
        back_part = prev_node

        # merge two parts by inserting nodes from back part into front part (backpart is always shorter)
        while back_part:
            # save next nodes
            front_part_next = front_part.next
            back_part_next = back_part.next

            # insert back part node into front part
            front_part.next = back_part
            back_part.next = front_part_next

            # update pointers
            back_part = back_part_next
            front_part = front_part_next