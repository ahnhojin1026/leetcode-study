# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a new linked list to store the merged result
        new_list = ListNode()
        cur = new_list

        while list1 is not None or list2 is not None:
            # if both lists have nodes to compare
            if list1 is not None and list2 is not None:
                # use smaller value node
                if list1.val < list2.val:
                    cur.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    cur.next = ListNode(list2.val)
                    list2 = list2.next
            # if only one list has nodes left
            elif list1 is None:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            elif list2 is None:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            cur = cur.next
        return new_list.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # heapq approach
        min_heap = []

        for i, lst in enumerate(lists):
            # add the minimum value of the list to the heap
            if lst:
                # add tuple (node value, list index, node) to avoid error between ListNodes
                heapq.heappush(min_heap, (lst.val, i, lst))
        
        ans_list = ListNode()
        cur = ans_list

        # merge nodes until heap is empty
        while min_heap:
            # pop the smallest node among heap
            val, i, node = heapq.heappop(min_heap)
            
            # put the node to the merged list
            cur.next = node
            cur = cur.next
            
            # update the heap with the next node from the same list
            if node.next:
                next_node = node.next
                heapq.heappush(min_heap, (next_node.val, i, next_node))
        
        return ans_list.next





        