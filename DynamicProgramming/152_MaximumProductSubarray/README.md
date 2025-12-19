# [LeetCode] 152. Maximum Product Subarray

## 📌 Topic
* Dynamic Programming
* Array

## 💡 Idea / Intuition
Finding the maximum product in a contiguous subarray is challenging due to **negative numbers**.
* Multiplying a positive number by a negative number makes it smaller.
* Multiplying a negative number by a negative number makes it larger (potentially the maximum).

## 📝 Approach
1.  Initialize `cur_max`, `cur_min`, and `ans` with the first element.
2.  Iterate from the second element:
    * **If `nums[i] >= 0`:**
        * The new max is `max(cur_max * nums[i], nums[i])`.
        * The new min is `min(cur_min * nums[i], nums[i])`.
    * **If `nums[i] < 0`:**
        * The new max comes from the previous min: `max(cur_min * nums[i], nums[i])`.
        * The new min comes from the previous max: `min(cur_max * nums[i], nums[i])`.
        * *Note:* Use a temporary variable (`new_cur_max`) to avoid using the updated max value when calculating the min.
    * Update the global maximum `ans`.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * Iterate through the array once.
* **Space Complexity:** $O(1)$
    * Only uses constant extra space (`cur_max`, `cur_min`, `ans`).