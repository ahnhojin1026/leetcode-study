# [LeetCode] 23. Merge k Sorted Lists

## 📌 Topic
* Heap (Priority Queue)
* Divide and Conquer
* Linked List

## 💡 Problem Overview
We need to merge $k$ sorted linked lists into a single sorted linked list.
A naive solution (merging one by one) would take $O(k \times N)$ time.
We can optimize this to **$O(N \log k)$** using two different approaches:
1.  **Divide & Conquer:** Merging lists in pairs (Tournament style).
2.  **Min-Heap:** Always selecting the smallest head node among $k$ lists.

## 📝 Approach 1: Divide and Conquer (Merge Sort Style)

### 🔹 Idea
Instead of merging lists sequentially ($L_1+L_2 \to +L_3 \dots$), we merge them in pairs simultaneously to reduce the number of merge steps.
* **Round 1:** Merge $(L_0, L_1), (L_2, L_3), \dots$
* **Round 2:** Merge results from Round 1.
* Repeat until only one list remains.
* This reduces the depth of merging to $\log k$.

## 📝 Approach 2 : Heapq
1.  **Initialize Heap:** Push the head node of every non-empty list into a Min-Heap.
    * **Tuple Structure:** `(node.val, i, node)`
    * *Note:* The index `i` is included to break ties when `node.val` is the same, avoiding direct comparison between `ListNode` objects (which causes TypeError in Python).
2.  **Extract & Link:**
    * Pop the smallest element (`node`) from the heap.
    * Attach it to the result list (`tail.next`).
    * If the popped node has a `next` node, push that `next` node into the heap.
3.  **Repeat:** Continue until the heap is empty.

## ⏱️ Complexity
* **Time Complexity:** $O(N \log k)$
    * $N$: Total number of nodes.
    * $k$: Number of linked lists.
    * Heap operations (push/pop) take $O(\log k)$. We perform this for every node.
* **Space Complexity - heap:** $O(k)$
    * The heap stores at most $k$ elements (one from each list) at any given time.
* **Space Complexity - divide & counquer:** $O(N)$
    * In merge two list function, new copy of list is created to save the original datas