# [LeetCode] 56. Merge Intervals

## 📌 Topic
* Array
* Sorting

## 💡 Idea / Intuition
The problem asks to merge all overlapping intervals.
Without sorting, we would have to compare every interval with every other interval ($O(N^2)$).

By **Sorting the intervals by their Start Time**, we gain a powerful property:
* For any interval we encounter, we only need to compare it with the **last merged interval** in our result list.
* If the current interval starts *after* the last merged interval ends, they don't overlap.
* If it starts *before* the last one ends, they overlap, and we merge them.

## 📝 Approach
1.  **Sort:** Sort `intervals` based on the **start time** (`x[0]`).
2.  **Iterate:** Initialize `ans` with the first interval. Loop through the rest:
    * **Overlap Check:** Check if the current interval's start (`curr[0]`) is $\le$ the last merged interval's end (`ans[-1][1]`).
    * **Merge:** If overlapping, extend the last interval's end to the maximum of both ends (`max(ans[-1][1], curr[1])`).
    * **No Overlap:** If not overlapping, simply append the current interval to `ans`.

## ⏱️ Complexity
* **Time Complexity:** $O(N \log N)$
    * Sorting takes $O(N \log N)$.
    * The linear scan takes $O(N)$.
* **Space Complexity:** $O(N)$
    * In the worst case (no overlapping intervals), we store all intervals in `ans`.
    * (Sorting logic depends on language implementation, Python's Timsort is $O(N)$).
