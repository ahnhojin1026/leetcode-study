# [LeetCode] 48. Rotate Image

## 📌 Topic
* Array
* Matrix
* Math (Geometry)

## 💡 Idea / Intuition
We need to rotate an $N \times N$ matrix 90 degrees clockwise **in-place**.

## 📝 Approach
1.  **Scope Selection:** We only need to iterate through a specific quadrant of the matrix (approx. $1/4$ of the cells) to avoid rotating the same cells multiple times.
    * Rows: $0$ to $\lceil N/2 \rceil - 1$
    * Cols: $0$ to $\lfloor N/2 \rfloor - 1$
2.  **4-Way Swap:** For each cell $(x, y)$, we perform a cyclic swap of 4 corresponding cells:
    * Save `Top-Left` to `temp`.
    * Move `Bottom-Left` $\rightarrow$ `Top-Left`
    * Move `Bottom-Right` $\rightarrow$ `Bottom-Left`
    * Move `Top-Right` $\rightarrow$ `Bottom-Right`
    * Move `temp` (Top-Left) $\rightarrow$ `Top-Right`

## ⏱️ Complexity
* **Time Complexity:** $O(N^2)$
    * We process each cell exactly once ($N^2 / 4$ operations $\times 4$ swaps).
* **Space Complexity:** $O(1)$
    * We modify the matrix in-place without allocating extra space.