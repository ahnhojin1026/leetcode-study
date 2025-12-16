# [LeetCode] 143. Reorder List

## 📌 Topic
* Linked List
* Two Pointers
* In-place Manipulation

## 💡 Idea / Intuition

To achieve **$O(1)$ space complexity**, we must solve this using pointer manipulation in three distinct steps.
> Initial approach : use a `Deque` (Double-ended Queue) satisfies the functional requirements but consumes $O(N)$ space.

## 📝 Approach
This problem is a combination of three classic Linked List problems:

1.  **Find the Middle:** * Use **Slow & Fast pointers**. When `fast` reaches the end, `slow` is at the middle.
    * **Critical Step:** Set `slow.next = None` to physically split the list into two independent halves.

2.  **Reverse the Second Half:**
    * Reverse the second part of the list in-place ($O(N)$).
    * This allows us to iterate the second half from the end towards the middle.

3.  **Merge (Zip) Two Lists:**
    * Iterate through both the first half and the reversed second half.
    * rewire the nodes in a zigzag pattern

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * Finding middle: $O(N/2)$
    * Reversing: $O(N/2)$
    * Merging: $O(N/2)$
    * Total is linear.
* **Space Complexity:** $O(1)$
    * We do not use any auxiliary data structures like Arrays or Deques. We only use a few pointers (`prev`, `curr`, `next`) for in-place manipulation.