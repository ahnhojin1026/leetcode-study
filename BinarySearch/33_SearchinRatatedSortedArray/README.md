# [LeetCode] 33. Search in Rotated Sorted Array

## 📌 Topic
* Binary Search
* Array

## 💡 Idea / Intuition
We need to search for a target in an array that has been rotated at some pivot.
The key insight is that for any split at `mid`, **at least one half (either left or right) must be sorted.**

## 📝 Approach
1.  Initialize `left` and `right` pointers.
2.  Loop while `left <= right`:
    * Calculate `mid`. If `nums[mid] == target`, return `mid`.
    * **Check Left Sorted:** If `nums[left] <= nums[mid]`:
        * If `nums[left] <= target < nums[mid]`, move `right` to `mid - 1`.
        * Otherwise, the target must be in the right half, so move `left` to `mid + 1`.
    * **Check Right Sorted:** Else (`nums[mid] < nums[left]`):
        * If `nums[mid] < target <= nums[right]`, move `left` to `mid + 1`.
        * Otherwise, move `right` to `mid - 1`.
3.  Return `-1` if not found.

## ⏱️ Complexity
* **Time Complexity:** $O(\log N)$
    * We eliminate half of the elements in each step, just like standard binary search.
* **Space Complexity:** $O(1)$
    * Iterative approach uses constant extra space.