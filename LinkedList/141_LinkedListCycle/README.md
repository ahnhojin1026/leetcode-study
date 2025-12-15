# [LeetCode] 141. Linked List Cycle

## 📌 Topic
* Linked List
* Two Pointers

## 💡 Idea / Intuition
We need to determine if a linked list has a cycle without using extra memory (i.e., $O(1)$ space).

1. **Slow Pointer :** Moves 1 step at a time.
2. **Fast Pointer :** Moves 2 steps at a time.
3. **Logic:**
    * If there is **no cycle**, the Fast pointer will reach the end (`None`) first.
    * If there is **a cycle**, the Fast pointer will eventually enter the cycle and "lap" (catch up to) the Slow pointer from behind. 
        * We can proof that two pointer will meet without jumping each other by relative velocity is **one edge at a time**

> Initial approach was to traverse through the linked list while tracking visted nodes using a `HashSet` ($O(N)$ space)

## 📝 Approach
1.  Initialize both `slow` and `fast` pointers at `head`.
2.  Loop while `fast` and `fast.next` are not `None` (to avoid null pointer exceptions).
3.  Move `slow` by 1 step (`slow.next`) and `fast` by 2 steps (`fast.next.next`).
4.  Check collision: If `slow == fast`, a cycle exists. Return `True`.
5.  If the loop finishes, the list has an end. Return `False`.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * If there is no cycle, we traverse the list once.
    * If there is a cycle, the Fast pointer will catch the Slow pointer within roughly one cycle length.
* **Space Complexity:** $O(1)$
    * We only use two pointers (`slow`, `fast`) regardless of the list size.