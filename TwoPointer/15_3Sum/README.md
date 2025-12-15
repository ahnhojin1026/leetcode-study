# [LeetCode] 15. 3Sum

## 📌 Topic
* Array
* Two Pointers
* Sorting

## 💡 Idea / Intuition
The problem asks to find all unique triplets that sum up to 0.
A naive approach using three nested loops would take $O(N^3)$ time, which is too slow.

We can optimize this to **$O(N^2)$** by **Sorting** the array first ($O(N \log N)$). This allows us to use the **Two Pointers** technique

**Duplicate Handling :**
Since the array is sorted, duplicate values are adjacent. We can simply skip them:
* Outer loop: If `nums[i] == nums[i-1]`, skip.
* Inner loop: After finding a valid triplet, move `left` and `right` until they point to new values

## 📝 Approach
1.  Sort the input array `nums`.
2.  Iterate through the array with index `i` from `0` to `n-2`:
    * **Pruning:** If `nums[i] > 0`, break (since the sum can never be 0).
    * **Skip Duplicates:** If `i > 0` and `nums[i] == nums[i-1]`, continue.
    * Initialize `left = i + 1` and `right = n - 1`.
    * While `left < right`:
        * Calculate `sum = nums[i] + nums[left] + nums[right]`.
        * If `sum < 0`: Increment `left` to increase the sum.
        * If `sum > 0`: Decrement `right` to decrease the sum.
        * If `sum == 0`:
            * Add the triplet to the answer.
            * Move both `left` and `right` inward.
            * **Skip inner duplicates** for both pointers.

## ⏱️ Complexity
* **Time Complexity:** $O(N^2)$
    * Sorting takes $O(N \log N)$.
    * The nested loop structure (outer loop + two pointers) runs in $O(N^2)$.
    * Total: $O(N^2)$.
* **Space Complexity:** $O(1)$ (or $O(N)$ depending on sorting implementation)
    * We ignore the space required for the output list.
    * Python's Timsort uses $O(N)$ space in the worst case.