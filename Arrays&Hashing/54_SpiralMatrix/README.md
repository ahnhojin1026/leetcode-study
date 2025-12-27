# [LeetCode] 54. Spiral Matrix

## 📌 Topic
* Matrix
* Simulation
* Array

## 💡 Idea / Intuition
The goal is to return all elements of the matrix in spiral order.
We can simulate the movement of a robot walking through the matrix.

## 📝 Approach
1.  **Direction Control:** Use a `delta` array `[[0,1], [1,0], [0,-1], [-1,0]]` to manage the movement direction.
2.  **Visited Marking (Space Optimization):**
    * Since the problem constraints state that values are between -100 and 100, we can mark visited cells with `-101` (or any out-of-range value).
    * This avoids using an extra $O(M \times N)$ `visited` matrix.
3.  **Simulation Loop:**
    * Iterate exactly $M \times N$ times (total number of elements).
    * If the next step is out of bounds or already visited (`-101`), change direction: `(direction + 1) % 4`.
    * Move to the next coordinate.

## ⏱️ Complexity
* **Time Complexity:** $O(M \cdot N)$
    * We visit every element exactly once.
* **Space Complexity:** $O(1)$
    * We modify the input matrix in-place for visited tracking.
    * (Note: If modifying input is forbidden, we need $O(M \cdot N)$ for a visited set or use the "Boundary Shrinking" approach).