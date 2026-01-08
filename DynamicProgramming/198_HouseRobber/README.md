# [LeetCode] 198. House Robber

## 📌 Topic
* Dynamic Programming
* Array

## 💡 Idea / Intuition
You are a professional robber planning to rob houses along a street.
However, adjacent houses have security systems connected.
**Constraint:** You cannot rob two adjacent houses.

For every house `i`, you have two choices:
1.  **Rob this house:** You gain `nums[i]`, but you must have come from `i-2` (skipping `i-1`). -> `nums[i] + dp[i-2]`
2.  **Skip this house:** You keep the maximum profit gained up to `i-1`. -> `dp[i-1]`

Therefore, the recurrence relation is:
$$DP[i] = \max(DP[i-1], DP[i-2] + nums[i])$$

## 📝 Approach
1.  **Base Cases:** Handle edge cases where `len(nums)` is 1 or 2 explicitly.
2.  **Space Optimization (Rolling Array):**
    * Instead of maintaining a full DP array of size `N`, we only need the previous two values to calculate the current one.
    * We use a fixed-size list `dp` of length 3 as a **sliding window (shift register)**.
    * `dp[0]`: Profit at `i-2`
    * `dp[1]`: Profit at `i-1`
    * `dp[2]`: Profit at `i` (Current)
3.  **Iterate & Shift:**
    * Update values: `dp[0] = dp[1]`, `dp[1] = dp[2]`.
    * Calculate new max: `dp[2] = max(dp[0] + nums[i], dp[1])`.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * We iterate through the houses once.
* **Space Complexity:** $O(1)$
    * We use a fixed-size array of 3, regardless of the number of houses.