# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    # Compare two subtree
    def compareSubtree(self, a: TreeNode, b: TreeNode) -> bool:
        # Base case
        if a is None and b is None:
            return True
        elif a is None:
            return False
        elif b is None:
            return False
        
        # Compare root value
        if a.val != b.val:
            return False
        # Compare left and right subtree recursively
        return self.compareSubtree(a.left ,b.left) and self.compareSubtree(a.right ,b.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Edge case
        if not root:
            return False
        

        ans = False
        # queue for BFS search of main tree
        queue = deque([])
        queue.append(root)

        while queue:
            cur = queue.popleft()
            if self.compareSubtree(cur, subRoot):
                ans = True
                break
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)

        return ans
        