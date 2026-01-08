# [LeetCode] 70. Climbing Stairs

## 📌 Topic
* Dynamic Programming (Space Optimization)
* Rolling Array / Sliding Window

## 💡 Idea / Intuition
You are climbing a staircase. It takes `n` steps to reach the top.
Each time you can either climb 1 or 2 steps.
This forms the **Fibonacci Sequence**: `ways(n) = ways(n-1) + ways(n-2)`.

A standard DP approach uses an array of size `n+1`, taking $O(n)$ space.
However, to calculate the current step, we **only need the previous two values**.
Therefore, we can optimize space to $O(1)$ by using a **fixed-size array of length 3** that acts as a sliding window.

## 📝 Approach
1.  **Base Cases:** Handle inputs `n=1` and `n=2` directly.
2.  **Rolling Array:** Initialize a list `dp` of size 3 to store `[step(i-2), step(i-1), step(i)]`.
    * `dp[1]`: Represents `step(i-1)`
    * `dp[2]`: Represents `step(i)` (Current)
3.  **Iterate & Shift:** From `i = 3` to `n`:
    * Shift values to the left: `dp[0] = dp[1]`, `dp[1] = dp[2]`.
    * Calculate new current: `dp[2] = dp[0] + dp[1]`.
4.  **Result:** The final answer is stored in `dp[2]`.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * We iterate from 3 to $N$ exactly once.
* **Space Complexity:** $O(1)$
    * We use a fixed-size array of 3, regardless of input size $N$.