# [LeetCode] 79. Word Search

## 📌 Topic
* Array / Matrix
* Backtracking
* Depth-First Search (DFS)

## 💡 Idea / Intuition
We need to find if a specific `word` exists in a 2D grid. The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically).
**Crucial Constraint:** The same letter cell may not be used more than once in a single word path.

Why **DFS** instead of BFS?
* **BFS:** Good for "shortest path". But here, we need to explore a specific path deeply to see if it matches the sequence. BFS would require maintaining a separate visited set for *each* path in the queue, which consumes exponential memory.
* **DFS:** Allows us to dive deep into one potential path. If it turns out to be wrong, we simply **backtrack** (step back) and try another direction. This is memory efficient ($O(L)$ stack depth, where $L$ is word length).

## 📝 Approach
1.  **Iterate:** Loop through every cell in the grid. If `board[i][j]` matches the first character of the `word`, start DFS.
2.  **DFS (Recursive Function):**
    * **Base Case:** If `cur_index` equals the length of the word, we found it! Return `True`.
    * **Boundary & Match Check:** If out of bounds OR the character doesn't match, return `False`.
    * **Mark Visited (In-place):** To save space, temporarily change `board[i][j]` to a special character (e.g., `#`) to mark it as visited for the current path.
    * **Explore:** Recursively call DFS for all 4 neighbors (up, down, left, right).
    * **Backtrack (Restore):** After the recursive calls return, **restore** `board[i][j]` to its original character. This allows other paths to use this cell later.
    * **Return:** If any neighbor returns `True`, propagate `True` up. Otherwise `False`.

## ⏱️ Complexity
* **Time Complexity:** $O(M \times N \times 4^L)$
    * $M, N$: Grid dimensions.
    * $L$: Length of the word.
    * For each cell, we explore 4 directions up to depth $L$. (With pruning, it's faster, but this is the worst case).
* **Space Complexity:** $O(L)$
    * We use recursion stack space proportional to the length of the word ($L$).
    * We optimized the visited array space to $O(1)$ by modifying the board in-place.