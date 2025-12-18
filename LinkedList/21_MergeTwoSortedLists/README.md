# [LeetCode] 21. Merge Two Sorted Lists

## 📌 Topic
* Linked List
* Merge Sort (Merge Step)

## 💡 Idea / Intuition
This problem corresponds to the **"Merge" phase** of the Merge Sort algorithm.

## 📝 Approach
1.  Initialize a `new_list` with a dummy node to act as the head of the result.
2.  Iterate while **either** `list1` or `list2` has nodes (`while list1 or list2`).
3.  **Compare and Create:**
    * If both lists have nodes: Compare `list1.val` and `list2.val`. Create a `new ListNode` with the smaller value and advance that list's pointer.
    * If only `list1` remains: Create a `new ListNode` with `list1.val` and advance.
    * If only `list2` remains: Create a `new ListNode` with `list2.val` and advance.
4.  Return `new_list.next` (skipping the dummy node).

## ⏱️ Complexity
* **Time Complexity:** $O(N + M)$
    * We iterate through both lists exactly once to process all elements.
* **Space Complexity:** $O(N + M)$
    * **Trade-off:** We create a new `ListNode` for every element in the merged list.
    * **Benefit:** This preserves the integrity of the original input lists (Immutable approach).