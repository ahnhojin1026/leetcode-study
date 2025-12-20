# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        result = []
        # queue for BFS
        queue = deque([])
        queue.append(root)
        while queue:
            node = queue.popleft()
            # append value
            # add children to queue
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            # Append value or "N" for null
            else:
                result.append("N")
        return ",".join(result)



        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        # split the string into list
        nodes = data.split(",")
        # traverse the list and build the tree from root
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        # index for nodes list
        i = 1
        while queue and i < len(nodes):
            parent = queue.popleft()
            # left child : append to queue if not null
            if nodes[i] != "N":
                left_node = TreeNode(int(nodes[i]))
                parent.left = left_node
                queue.append(left_node)
            i += 1
            
            # right child : if exists, append to queue if not null
            if i < len(nodes) and nodes[i] != "N":
                right_node = TreeNode(int(nodes[i]))
                parent.right = right_node
                queue.append(right_node)
            i += 1
            
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))