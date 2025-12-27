# [LeetCode] 53. Maximum Subarray

## 📌 Topic
* Dynamic Programming
* Divide and Conquer (Mention only)
* **Kadane's Algorithm** (Best Approach)

## 💡 Idea / Intuition
We need to find the contiguous subarray with the largest sum.
A brute force approach would check all subarrays in $O(N^2)$, which is too slow.

The optimal approach is **Kadane's Algorithm**. The core idea is:
* Iterate through the array and keep a running sum (`cur_max`).
* At each position `n`, we make a choice:
    1.  **Extend** the existing subarray: `cur_max + n`
    2.  **Start New**: If the previous `cur_max` was negative (dragging us down), it's better to discard it and start a new subarray from `n`.

    📝 Approach
1.  **Initialize:**
    * `cur_max` to 0 (or first element).
    * `max_sum` to `nums[0]` (to handle arrays with all negative numbers correctly).
2.  **Iterate:** Loop through each number `n` in `nums`.
3.  **Update Current Max:** `cur_max = max(cur_max + n, n)`
    * This implicitly handles the logic: "If `cur_max` < 0, reset to `n`".
4.  **Update Global Max:** `max_sum = max(max_sum, cur_max)`

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * We pass through the array exactly once.
* **Space Complexity:** $O(1)$
    * We only use two variables (`cur_max`, `max_sum`) regardless of input size.