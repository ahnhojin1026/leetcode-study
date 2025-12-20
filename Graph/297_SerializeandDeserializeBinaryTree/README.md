# [LeetCode] 297. Serialize and Deserialize Binary Tree

## 📌 Topic
* Binary Tree
* Breadth-First Search (BFS)
* Design / String Manipulation

## 💡 Idea / Intuition
We need to convert a tree structure into a string (Serialize) and reconstruct it back (Deserialize).
Using **BFS (Level Order Traversal)** is intuitive because it processes nodes layer by layer, similar to how arrays represent heaps.

The critical challenge is handling `None` (null) nodes to preserve the structure. We mark `None` as `"N"` (or any placeholder) to know when a branch terminates.

## 📝 Approach
### 1. Serialize (Tree -> String)
* Use a **Queue** for standard BFS traversal.
* If a node is `None`, append `"N"` to the result list.
* If a node exists, append its value and add its children (even if they are `None`) to the queue.
* Finally, join the list with a delimiter (e.g., `,`) to form the string.

### 2. Deserialize (String -> Tree)
* Split the string by the delimiter to get a list of values.
* Use a **Queue** to store parent nodes waiting for their children.
* Use an **Index Pointer (`i`)** to traverse the values list.
* **Logic:**
    1. Pop a `parent` from the queue.
    2. Read `values[i]` (Left Child): If not `"N"`, create node, link to `parent.left`, and push to queue.
    3. Read `values[i+1]` (Right Child): If not `"N"`, create node, link to `parent.right`, and push to queue.
    4. Repeat until the queue is empty.

### ⚠️ Key Learning (Why not use Index Math?)
* Initially, I tried using the Heap indexing method (`left = 2*i`, `right = 2*i+1`).
* **Problem:** If the tree is skewed (e.g., a linked list of depth 1000), the array index grows exponentially ($2^{1000}$), causing **Memory Limit Exceeded (MLE)**.
* **Solution:** Instead of calculating indices, use a **Queue + Iterator** approach to process nodes sequentially as they appear in the level-order list.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * We visit every node exactly once during both serialization and deserialization.
* **Space Complexity:** $O(N)$
    * **Serialize:** The queue holds the widest level of the tree, and the result string stores $N$ nodes.
    * **Deserialize:** The queue and the node list both scale linearly with $N$.