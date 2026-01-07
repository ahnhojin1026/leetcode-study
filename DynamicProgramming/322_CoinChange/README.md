# [LeetCode] 322. Coin Change

## 📌 Topic
* Dynamic Programming (DP)
* Breadth-First Search (BFS)

## 💡 Idea / Intuition
We want to find the minimum number of coins to make up a specific `amount`.
This is a classic optimization problem where **Greedy fails** (e.g., coins=[1, 3, 4], amount=6 -> Greedy takes 4+1+1 (3 coins), but Optimal is 3+3 (2 coins)).

We must explore all valid combinations, but efficiently.

## ⚔️ Evolution of Approach (My Journey)

### 1. The Brute Force: Backtracking (❌ Time Limit Exceeded)
* **Idea:** Recursively try every coin and explore all paths.
* **Problem:** It creates a massive recursion tree with many repeated calculations.
* **Complexity:** Exponential $O(K^N)$ ($K$=coins, $N$=amount).

### 2. The Optimization: Top-Down DP with Memoization (⚠️ Python TLE)
* **Idea:** Add a `memo` dictionary to store results of `dfs(rem)` so we don't re-calculate.
* **Problem:** While theoretically correct ($O(N \cdot K)$), Python's heavy **recursion overhead** and **stack depth limit** caused it to be slower than acceptable for large inputs.

### 3. The Final Solution: Bottom-Up DP (✅ Accepted)
* **Idea:** Instead of recursion, we build the solution iteratively from 0 up to `amount`.
* **Logic:**
    * `dp[i]` stores the min coins for amount `i`.
    * Transition: `dp[i] = min(dp[i], dp[i - coin] + 1)`
    * If `dp[i - coin]` is unreachable (`-1`), we skip it.

## 📝 Approach (Bottom-Up)
1.  **Initialize:** Create a `dp` array of size `amount + 1` filled with `-1`. Set `dp[0] = 0`.
2.  **Iterate:** Loop from `1` to `amount`.
3.  **Check Previous States:** For each coin `c`:
    * If `i - c >= 0` AND `dp[i - c]` is reachable (not `-1`):
        * If `dp[i]` was `-1` (first valid path found), set `dp[i] = dp[i - c] + 1`.
        * Else, update `dp[i]` with the minimum: `min(dp[i], dp[i - c] + 1)`.
4.  **Result:** Return `dp[amount]`.

## ⏱️ Complexity
* **Time Complexity:** $O(S \times N)$
    * $S$: Amount to change.
    * $N$: Number of coin types.
* **Space Complexity:** $O(S)$
    * Array of size `amount + 1`.