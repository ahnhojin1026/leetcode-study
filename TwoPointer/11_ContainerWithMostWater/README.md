# [LeetCode] 11. Container With Most Water

## 📌 Topic
* Two Pointers
* Greedy Algorithm
* Array

## 💡 Idea / Intuition
* Use `Two Pointer Method` for `O(N)` solution
* Starting from the widest case, shrink with greedy approach
    * Water height is determined to the shorter height
    * When shrinking, among two height shrinking taller one is meaningless (Greedy approach)
        * if the inside height is taller, it doesn't matter - opposite height is still limit, only width decreased
        * if the inside height is shorter, both height and width is decreased

## 📝 Approach
1.  Initialize two pointers: `left` at the beginning (`0`) and `right` at the end (`len(height) - 1`).
2.  Initialize `max_amount_water` to 0.
3.  Loop while `left < right`:
    * Calculate the current area: `min(height[left], height[right]) * (right - left)`.
    * Update `max_amount_water` if the current area is larger.
    * **Move Pointer:** If `height[left] < height[right]`, increment `left`. Otherwise, decrement `right`.
4.  Return `max_amount_water`.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * The pointers start at both ends and move towards each other. We traverse the array exactly once.
* **Space Complexity:** $O(1)$
    * We use only a few variables (`left`, `right`, `max_amount_water`) for storage.