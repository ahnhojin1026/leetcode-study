# [LeetCode] 73. Set Matrix Zeroes

## 📌 Topic
* Array
* Matrix
* Space Optimization (In-place)

## 💡 Idea / Intuition
We need to set entire rows and columns to 0 if an element is 0.
A naive approach uses $O(M+N)$ space to store which rows/cols need to be zeroed.
However, to achieve **$O(1)$ space complexity**, we can use the matrix itself as storage.

We use the **first row** and **first column** of the matrix as "markers" (or flags).
* If `matrix[i][j]` is 0, we mark `matrix[i][0]` and `matrix[0][j]` as 0.
* Exception: Since `matrix[0][0]` is the intersection of the first row and first column, we use separate boolean variables (`row0`, `col0`) to track the status of the first row/column strictly.

## 📝 Approach
1.  **Initialization:** Flag variables `row0` and `col0` to `False`.
2.  **Marking Phase:** Iterate through the entire matrix.
    * If `matrix[i][j] == 0`:
        * Update `row0`/`col0` flags if `i` or `j` is 0.
        * Mark the headers: `matrix[i][0] = 0`, `matrix[0][j] = 0`.
3.  **Inner Matrix Processing:** Iterate from `(1, 1)` to `(m, n)`.
    * If either the row header (`matrix[i][0]`) or col header (`matrix[0][j]`) is 0, set `matrix[i][j] = 0`.
4.  **Edge Handling:** Process the first row and first column last using `row0` and `col0` flags.
    * **Note:** We must process the inner matrix *before* handling the first row/col to avoid overwriting the markers needed for the inner cells.

## ⏱️ Complexity
* **Time Complexity:** $O(M \times N)$
    * We traverse the matrix twice (once for marking, once for setting zeros).
* **Space Complexity:** $O(1)$
    * We use the input matrix itself for storage and only a few constant variables.