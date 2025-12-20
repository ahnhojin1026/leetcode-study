# [LeetCode] 39. Combination Sum

## 📌 Topic
* Backtracking
* Recursion

## 💡 Idea / Intuition
We need to find all unique combinations where the sum of numbers equals the `target`.
The key constraints are:
1.  **Unlimited Usage:** The same number can be chosen multiple times.
2.  **Combination:** The order does not matter (`[2, 2, 3]` is the same as `[3, 2, 2]`).

This suggests a **DFS (Depth-First Search)** approach on a decision tree where at each step, we decide whether to include the current candidate again or move to the next candidate.

## 📝 Approach
1.  **State Definition:** The recursive function needs to track:
    * `start_index`: To ensure we only pick current or subsequent numbers (avoiding duplicates like `[2, 3]` and `[3, 2]`).
    * `cur_sum`: The sum of the current path.
    * `path`: The list of numbers selected so far.
2.  **Base Cases:**
    * **Success:** `cur_sum == target` -> Add `path` to results.
    * **Fail:** `cur_sum > target` -> Stop recursion (Pruning).
3.  **Recursive Step:**
    * Iterate through `candidates` starting from `start_index`.
    * Crucially, when making a recursive call, pass `i` (not `i + 1`) as the new `start_index`. This allows reusing the same element.
    * **Implementation Note:** Using `path + [candidate]` creates a new list instance for the next recursion, eliminating the need for manual backtracking (`pop()`).

## ⏱️ Complexity
* **Time Complexity:** $O(N^{\frac{T}{M}})$
    * $N$: Number of candidates.
    * $T$: Target value.
    * $M$: Minimum value in candidates.
    * In the worst case, the height of the tree is $T/M$, and at each step, we branch out $N$ times.
* **Space Complexity:** $O(\frac{T}{M})$
    * Maximum depth of the recursion stack.