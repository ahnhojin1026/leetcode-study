# [LeetCode] 133. Clone Graph

## 📌 Topic
* Graphs
* Breadth-First Search (BFS) / Depth-First Search (DFS)
* Hash Table (Design)

## 💡 Idea / Intuition
* Traversal the given graph and make a copy (BFS/DFS)

## 📝 Approach (BFS/DFS)
1. **Edge Case** If the input in `None` return `None`
2. **Initialization:** 
    * Create a dictionary `copied_graph` to act as the **Lookup Table**.
        * Key : address to the given Node
        * Value : new address to the cloned Node
    * BFS : Create a deque for BFS search initalized to the starting node (queue)
    * DFS : Create a deque for DFS search initalized to the starting node (stack)
3. **Traversal**
    * While the queue/stack is non-empty pop the front *original* node
    * Iterate through node neighbor
        * if the neighbor not cloned before, clone and add it to `copied_graph`
        * append the cloned neighbor node to the current node's neighbor list 
4.  **Return:** The clone of the starting node

## ⏱️ Complexity
* **Time Complexity:** $O(V + E)$
    * $V$: Vertices (Nodes), $E$: Edges.
    * We visit every node once and iterate through every edge once to establish connections.
* **Space Complexity:** $O(V)$
    * The `copied_graph` hash map stores all $V$ nodes.
    * Space Complexity *BFS vs DFS*
    * The BFS queue stores up to $O(W)$ nodes, where $W$ is the width of the graph (bounded by $V$).
    * The DFS stack stores up to $O(D)$ nodes, where $D$ is the depth of the graph (bounded by $V$).
