# [LeetCode] 153. Find Minimum in Rotated Sorted Array

## 📌 Topic
* Binary Search
* Array

## 💡 Idea / Intuition
In a rotated sorted array, the minimum element represents a "drop" or "cliff" where the increasing sequence is interrupted.

## 📝 Approach
1.  **Sorted Check:** If `nums[left] < nums[right]`, the array is not rotated (or rotated n times). Return `nums[left]`.
2.  **Binary Search:** Loop while `left < right - 1` (stop when pointers are adjacent).
    * **Immediate Drop Detection:** If `nums[mid] > nums[mid+1]`, then `mid+1` is definitely the minimum. Return it immediately.
    * **Adjust Bounds:**
        * If `nums[mid] < nums[left]`: The middle is in the second (lower) increasing segment. The minimum is to the **left**. (`right = mid`)
        * Else: The middle is in the first (higher) increasing segment. The minimum is to the **right**. (`left = mid`)
3.  **Final Return:** If the loop ends, `nums[right]` will hold the minimum value.

## ⏱️ Complexity
* **Time Complexity:** $O(\log N)$
    * Standard binary search halves the search space each iteration.
* **Space Complexity:** $O(1)$
    * Only pointer variables are used.