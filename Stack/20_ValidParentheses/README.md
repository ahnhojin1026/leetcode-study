# [LeetCode] 20. Valid Parentheses

## 📌 Topic
* Stack
* String

## 💡 Idea / Intuition
The problem asks to validate if the brackets are closed in the correct order.
Since the innermost bracket must be closed first (Last-In, First-Out), a **Stack** is the perfect data structure.

**Optimization:**
A valid parentheses string must always have an even number of characters. If `len(s)` is odd, we can immediately return `False` without checking.

## 📝 Approach
1.  **Early Exit:** Check if `len(s)` is odd. If so, return `False`.
2.  Initialize a Stack (using `deque` or `list`).
3.  Iterate through the string:
    * **Open Brackets** (`(`, `{`, `[`): Push onto the stack.
    * **Close Brackets** (`)`, `}`, `]`):
        * Check if the stack is empty (invalid case).
        * Pop the top element and check if it matches the current closing bracket.
4.  **Final Check:** After the loop, the stack must be empty. If elements remain, it means there are unclosed brackets.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * We traverse the string exactly once. Push and pop operations are $O(1)$.
* **Space Complexity:** $O(N)$
    * In the worst case (e.g., all open brackets), the stack size grows linearly with the input size.