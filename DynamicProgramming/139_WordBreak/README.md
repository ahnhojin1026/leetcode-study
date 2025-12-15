# [LeetCode] 139. Word Break

## 📌 Topic
* Dynamic Programming (1-Dimensional)
* String Manipulation

## 💡 Idea / Intuition
We need to determine if the string `s` can be broken down into valid words.
Instead of checking every permutation (which is exponential), we can use **Dynamic Programming**.

> **Refactoring Note:**
> Initially solved using **Interval DP (2D array)** with $O(N^3)$ complexity.
> Optimized to **Linear DP (1D array)** to reduce space complexity to $O(N)$ and remove redundant checks.

## 📝 Approach
1.  Convert `wordDict` to a `Set` for $O(1)$ lookup time.
2.  Initialize a boolean array `dp` of size $N$.
3.  Iterate through the string with index `i` (end index of current substring):
    * **Base Check:** If `s[0...i+1]` is in the set, set `dp[i] = True`.
    * **Split Check:** Iterate `mid` from `0` to `i-1`. If `dp[mid]` is True and the remaining substring `s[mid+1...i+1]` is in the set, set `dp[i] = True` and **break** (pruning).
4.  Return `dp[n-1]`.

# ⏱️ Complexity
* **Time Complexity:** $O(N^3)$
    * Nested loops give $O(N^2)$ iterations.
    * String slicing `s[mid+1:i+1]` and hashing takes $O(N)$ inside the loop.
    * *Note: Conceptually it's an $O(N^2)$ DP structure.*
* **Space Complexity:** $O(N)$
    * We use a 1D array `dp` of size $N$.