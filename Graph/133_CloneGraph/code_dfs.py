"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if nothing is given
        if node is None:
            return None

        # Dictionary to record visted node plus, lookup table for address of node 
        # Key : addrss of the oringal node
        # Value : address of the copied node
        copied_graph = {}

        # stack for dfs search
        dfs = deque([node])

        # append the first node to the stack
        copied_graph[node] = Node(node.val)
        while dfs:
            # pop the first (orignal) node from the stack
            cur = dfs.pop()

            for neighbor in cur.neighbors:
                # if the neighbor is not copied yet
                if neighbor not in copied_graph:
                    # make a copy
                    copied_graph[neighbor] = Node(neighbor.val)
                    # append to the dfs stack for further search
                    dfs.append(neighbor)
                
                # the copied current node
                cur_copied_node = copied_graph[cur]
                # append to the copied current node's neighbor
                cur_copied_node.neighbors.append(copied_graph[neighbor])


        return copied_graph[node]
        
