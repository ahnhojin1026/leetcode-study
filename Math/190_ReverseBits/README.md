# [LeetCode] 190. Reverse Bits

## 📌 Topic
* Bit Manipulation

## 💡 Idea / Intuition
We need to reverse the binary representation of a 32-bit unsigned integer.
Think of it as processing a stream of bits:
1.  Extract the last bit (Least Significant Bit, LSB) from the input `n`.
2.  Push this bit into the result `ans`.
3.  Shift `ans` to the left to make room for the next bit.
4.  Shift `n` to the right to process the next bit.

This is similar to reversing a string or an array but done using bitwise operators.

## 📝 Approach
1.  **Initialize:** `ans = 0`.
2.  **Iterate:** Loop exactly 32 times (since it's a 32-bit integer).
3.  **Shift Result:** `ans = ans << 1`. (Push existing bits to the left).
4.  **Extract & Add:** * Get the last bit of `n`: `n & 1`.
    * Add it to the LSB of `ans`: `ans | (n & 1)` (or `ans +` if the LSB is 0).
    * *Note:* In code, we usually combine steps 3 and 4: `ans = (ans << 1) | (n & 1)`.
5.  **Shift Input:** `n = n >> 1`. (Discard the processed bit).
6.  **Return:** `ans`.

## ⏱️ Complexity
* **Time Complexity:** $O(1)$
    * The loop runs exactly 32 times, regardless of the input value.
* **Space Complexity:** $O(1)$
    * Only a single variable `ans` is used.