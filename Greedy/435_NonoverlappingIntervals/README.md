# [LeetCode] 435. Non-overlapping Intervals

## 📌 Topic
* Greedy
* Sorting
* Interval Scheduling

## 💡 Idea / Intuition
The goal is to remove the minimum number of intervals to make the rest non-overlapping.
This is equivalent to finding the **maximum number of non-overlapping intervals** and subtracting that from the total count.

To maximize the number of non-overlapping intervals, we should always pick the interval that **finishes earliest**.
* **Why?** Finishing early leaves the maximum possible remaining time for subsequent intervals, increasing the chance to fit more in.

## 📝 Approach
1.  **Sort:** Sort the intervals based on their **end times** in ascending order.
2.  **Iterate & Select:**
    * Initialize `cur_end` with the end time of the first interval.
    * Iterate through the rest of the intervals.
    * **Case 1 (Non-overlapping):** If the current interval starts after or exactly when the previous one ends (`start >= cur_end`), it means we can keep this interval. Update `cur_end` to the current interval's end.
    * **Case 2 (Overlapping):** If the current interval starts before the previous one ends, it overlaps. Since we already picked the one that finishes earlier (thanks to sorting), we discard the current one (increment `ans`).

## ⏱️ Complexity
* **Time Complexity:** $O(N \log N)$
    * Sorting the intervals takes $O(N \log N)$.
    * The linear scan takes $O(N)$.
* **Space Complexity:** $O(1)$