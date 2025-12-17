# [LeetCode] 19. Remove Nth Node From End of List

## 📌 Topic
* Linked List
* Two Pointers (Sliding Window)

## 💡 Idea / Intuition
The challenge is to delete the $N$-th node from the end **in a single pass** ($O(N)$).
Since we don't know the length of the list beforehand, we can't simply iterate `Length - N` times. -> Use two pointer method

## 📝 Approach
1.  Initialize `slow` and `fast` pointers at `head`.
2.  **Create Gap:** Move `fast` pointer $N$ steps forward.
3.  **Handle Edge Case (Head Removal):**
    * If `fast` becomes `None` immediately after step 2, it means $N$ equals the list length. We need to remove the `head`. Return `head.next`.
4.  **Slide Window:**
    * Move both `slow` and `fast` one step at a time until `fast` reaches the end (`None`).
    * Keep track of `slow_prev` (node before `slow`) to perform deletion.
5.  **Delete Node:**
    * Update `slow_prev.next` to skip `slow` (`slow.next`).

## ⏱️ Complexity
* **Time Complexity:** $O(L)$
    * $L$ is the number of nodes. We traverse the list exactly once.
* **Space Complexity:** $O(1)$
    * We only use a few pointers (`slow`, `fast`, `slow_prev`).