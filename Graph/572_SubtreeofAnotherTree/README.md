# [LeetCode] 572. Subtree of Another Tree

## 📌 Topic
* Tree
* Depth-First Search (DFS) / Breadth-First Search (BFS)
* Binary Tree

## 💡 Idea / Intuition
We need to check if the tree `subRoot` is a subtree of `root`.
This means there must be some node in `root` such that the subtree starting from that node is **identical** to `subRoot`.

The problem can be broken down into two parts:
1.  **Traversal:** Visit every node in the main `root` tree (using BFS or DFS).
2.  **Comparison:** For each visited node, check if the tree rooted there is identical to `subRoot`.

## 📝 Approach
1.  **Helper Function (`compareSubtree`):**
    * Checks if two binary trees are identical.
    * Returns `True` if both are `None`.
    * Returns `False` if only one is `None` or their values differ.
    * Recursively checks left and right children.
2.  **Main Function (`isSubtree`):**
    * Use **BFS (Queue)** to traverse the `root` tree level by level.
    * For each node `cur` extracted from the queue:
        * Call `compareSubtree(cur, subRoot)`.
        * If it returns `True`, we found the subtree! Return `True` immediately.
        * Add valid children (`cur.left`, `cur.right`) to the queue for further traversal.
    * If the queue becomes empty and no match is found, return `False`.

## ⏱️ Complexity
* **Time Complexity:** $O(M \times N)$
    * $M$: Number of nodes in `root`.
    * $N$: Number of nodes in `subRoot`.
    * In the worst case, for every node in `root`, we might perform a full comparison of size $N$.
* **Space Complexity:** $O(M)$
    * The queue for BFS can store up to $O(M)$ nodes (width of the tree).
    * The recursion stack for comparison takes $O(N)$ (height of `subRoot`).