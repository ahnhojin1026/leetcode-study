# [LeetCode] 57. Insert Interval

## 📌 Topic
* Array
* Interval

## 💡 Idea / Intuition
The problem asks to insert a new interval into a sorted list of non-overlapping intervals and merge if necessary.
Since the input `intervals` is already **sorted**, we can process the list in a single pass ($O(N)$) without resorting.

We can categorize the existing intervals into three types relative to the `newInterval`:
1.  **Strictly Left:** Ends before the new interval starts. (Add to result)
2.  **Strictly Right:** Starts after the new interval ends. (Add new interval, then add the rest)
3.  **Overlapping:** Merges with the new interval. (Update `newInterval` boundaries)

## 📝 Approach
1.  **Iterate:** Loop through each interval in the input list.
2.  **Case 1 (Left):** If the current interval ends before `newInterval` starts (`interval[1] < newInterval[0]`), it has no interaction. Append it to `ans`.
3.  **Case 2 (Right):** If the current interval starts after `newInterval` ends (`interval[0] > newInterval[1]`), it means we found the spot for `newInterval`.
    * Append the (possibly merged) `newInterval`.
    * Append the current interval and **all remaining intervals** (`intervals[i:]`).
    * Return immediately.
4.  **Case 3 (Overlap):** If neither above, they overlap.
    * Merge them by updating `newInterval`: `start = min`, `end = max`.
    * **Do not append yet**, because it might overlap with the *next* interval too.
5.  **Finalize:** If the loop finishes without returning (meaning `newInterval` was merged with the last elements or extends to the very end), append `newInterval` to `ans`.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * We iterate through the list exactly once.
* **Space Complexity:** $O(N)$
    * To store the result list.