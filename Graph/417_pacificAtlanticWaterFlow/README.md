# [LeetCode] 417. Pacific Atlantic Water Flow

## 📌 Topic
* Graph (BFS/DFS)
* Matrix
* Breath-First Search (BFS)

## 💡 Idea / Intuition
The naive approach involves iterating through every cell and checking if water can flow to both oceans, which results in redundant calculations ($O((MN)^2)$).

## 📝 Approach
1.  **Initialize Queues:** Create starting queues for Pacific (top/left edges) and Atlantic (bottom/right edges).
2.  **BFS Function:** Implement a helper function that takes starting cells and returns a set of reachable cells.
    * Condition to move: `next_height >= current_height` (Climbing up).
    * Track visited cells to avoid cycles and redundant processing.
3.  **Intersection:** Run BFS for both oceans to get two sets: `pacific_reachable` and `atlantic_reachable`.
4.  **Result:** Return the cells present in both sets (`pacific_reachable & atlantic_reachable`).

## ⏱️ Complexity
* **Time Complexity:** $O(M \times N)$
    * In the worst case, each cell is visited twice (once for the Pacific BFS, once for the Atlantic BFS).
* **Space Complexity:** $O(M \times N)$
    * We use Sets and Queues to store visited cells, which can store up to $M \times N$ elements.