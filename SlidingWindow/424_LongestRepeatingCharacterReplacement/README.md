# [LeetCode] 424. Longest Repeating Character Replacement

## 📌 Topic
* Sliding Window
* Two Pointers

## 💡 Idea / Intuition
The problem asks for the longest substring where we can replace at most `k` characters to make all characters in the substring the same.

Instead of checking every possible substring ($O(N^2)$), we can use a **Sliding Window** approach.
A window is valid if:
$$\text{(Window Length)} - \text{(Count of Most Frequent Char)} \le k$$

## 📝 Approach
1.  Initialize `left` pointer, `max_len`, and a frequency array `char_count`.
2.  Iterate with `right` pointer to expand the window:
    * Increment the count of `s[right]`.
    * Update `max_count`: This tracks the frequency of the most dominant character found so far in a valid window context.
        * *Optimization:* Instead of scanning the entire `char_count` array ($O(26)$), simply compare `max_count` with the updated count of the current character ($O(1)$).
3.  **Validation Check:**
    * If `(Window Length) - max_count > k`: The window is invalid.
    * Shrink the window from the `left` until it becomes valid again.
4.  Update `max_len` with the valid window size.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * The `right` pointer moves $N$ times.
    * The `left` pointer moves at most $N$ times.
    * Inner operations are $O(1)$ (thanks to the optimization).
* **Space Complexity:** $O(1)$
    * We use a fixed-size array for uppercase English letters.