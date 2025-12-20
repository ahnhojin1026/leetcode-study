# [LeetCode] 295. Find Median from Data Stream

## 📌 Topic
* Heap (Priority Queue)
* Design
* Two Heaps Pattern

## 💡 Idea / Intuition
To find the median efficiently in a stream of numbers, we need quick access to the middle elements.
Sorting the entire array every time takes $O(N \log N)$, which is too slow.

Instead, we can maintain two heaps to split the data into two halves:
1.  **Small Heap (Max-Heap):** Stores the smaller half of the numbers. The root is the largest of the small numbers (left side of median).
2.  **Large Heap (Min-Heap):** Stores the larger half of the numbers. The root is the smallest of the large numbers (right side of median).

If we balance the sizes of these two heaps, the median will always be at the roots.

## 📝 Approach
1.  **Initialize:**
    * `small_heap`: Max-Heap (simulated using negative values in Python).
    * `large_heap`: Min-Heap.
2.  **Add Number (`addNum`):**
    * **Strategy:** Distribute numbers based on the current total count (Odd/Even) to maintain size balance.
        * If total count is **Even**, push to `small_heap`.
        * If total count is **Odd**, push to `large_heap`.
    * **Correction (Swap):** After pushing, if the max of `small_heap` is greater than the min of `large_heap` (Boundary violation), **swap** the top elements of both heaps to restore order.
    * *Edge Case:* If it's the very first element, simply push and return (to avoid accessing empty `large_heap`).
3.  **Find Median (`findMedian`):**
    * If sizes are equal: The stream has an even number of elements. Return the average of both roots.
    * If sizes are different: The stream has an odd number of elements. `small_heap` will always have one more element (due to the logic). Return the root of `small_heap`.



## ⏱️ Complexity
* **Time Complexity:**
    * `addNum`: $O(\log N)$ (Heap push/pop operations).
    * `findMedian`: $O(1)$ (Accessing roots).
* **Space Complexity:** $O(N)$
    * To store elements in the heaps.