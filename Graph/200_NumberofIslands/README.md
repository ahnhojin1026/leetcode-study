# [LeetCode] 200. Number of Islands

## 📌 Topic
* Graph Theory
* Breadth-First Search (BFS)
* Matrix Traversal

## 💡 Idea / Intuition
The problem asks us to count the number of connected components of '1's (land) in a 2D grid.
We can treat the 2D grid as an undirected graph where:
* Nodes: Cells containing '1'.
* Edges: Adjacent connections (up, down, left, right).

The goal is to find the number of **disjoint sets** (islands).
We iterate through the grid, and whenever we find a piece of unvisited land, we trigger a traversal (BFS) to find (and mark) all connected lands belonging to that island.

## 📝 Approach
1.  **Iterate:** Loop through every cell `(i, j)` in the grid.
2.  **Trigger BFS:** If we encounter land (`grid[i][j] == '1'`), it means we found a new island.
    * Increment the island counter (`ans`).
    * Start a BFS from this cell to visit the entire island.
3.  **Space Optimization (In-place):**
    * Instead of using a separate `visited` array (which takes $O(M \times N)$ space), we **mutate the grid directly**.
    * When a land cell is added to the queue, we change its value from `"1"` to `"#"` (or `"0"`). This marks it as visited and prevents reprocessing.
4.  **BFS Traversal:**
    * Use a `deque` for efficient FIFO operations.
    * Explore 4 directions using a directional array (`delta`).
    * Valid neighbors (within bounds and equals `"1"`) are added to the queue and immediately marked as visited.

## ⏱️ Complexity
* **Time Complexity:** $O(M \times N)$
    * Each cell is visited a constant number of times.
* **Space Complexity:** $O(\min(M, N))$
    * **Queue:** In the worst case (e.g., the entire grid is land), the BFS queue can grow up to $\min(M, N)$.
    * **Auxiliary:** $O(1)$ effectively, since we removed the `visited` matrix by modifying the input grid.