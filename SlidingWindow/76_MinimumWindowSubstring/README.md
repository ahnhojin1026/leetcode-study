# [LeetCode] 76. Minimum Window Substring

## 📌 Topic
* String
* Sliding Window
* Hash Table (Dictionary)
* Two Pointers

## 💡 Idea / Intuition
The problem asks for the **shortest substring** in `s` that contains all characters from `t` (including duplicates).
Using a Brute Force approach ($O(N^2)$) is inefficient. Instead, we use the **Sliding Window** technique to solve it in linear time $O(N)$.

The core philosophy is **"Expand to satisfy, Contract to optimize"**:
1.  **Expand (`Right`):** Move the right pointer to ingest characters until the window becomes "valid" (contains all required characters from `t`).
2.  **Contract (`Left`):** Once valid, move the left pointer to eject characters. This shrinks the window to find the **minimum length**. We stop shrinking when the window becomes invalid again.

## 📝 Approach
1.  **Frequency Map:** Use a hash map (`t_dict`) to store the count of each character in `t`. This serves as our "checklist".
2.  **Variables:**
    * `s_dict`: Tracks character counts in the current window.
    * `exact`: Tracks how many unique characters have met the required count in `t`.
    * `required`: The total number of unique characters in `t`.
3.  **Algorithm:**
    * Iterate `right` pointer over `s`. Add `s[right]` to `s_dict`.
    * If `s[right]` matches the count in `t_dict`, increment `exact`.
    * **While `exact == required` (Valid Window):**
        * Update the result (`min_len`, `start_pos`) if the current window is smaller.
        * Remove `s[left]` from the window (`s_dict` decrement).
        * If the removal breaks the validity (`s_dict[char] < t_dict[char]`), decrement `exact`.
        * Increment `left` to shrink.
4.  **Edge Case:** If `min_len` remains infinity, return `""`.

## ⏱️ Complexity
* **Time Complexity:** $O(N + M)$
    * $N = |s|$, $M = |t|$.
    * Although there is a nested `while` loop, both `left` and `right` pointers increase monotonically. Each character is visited at most twice (once added, once removed).
* **Space Complexity:** $O(1)$ (Technically $O(K)$)
    * The dictionaries store at most the size of the character set (e.g., 52 for English letters), which is constant space.