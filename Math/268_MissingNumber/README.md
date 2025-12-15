# [LeetCode] 268. Missing Number

## 📌 Topic
* Array
* Math
* Bit Manipulation

## 💡 Idea / Intuition
We have a range of numbers `[0, n]` and one number is missing from the array.
Instead of sorting ($O(N \log N)$) or using a HashSet ($O(N)$ Space), we can use basic mathematics.

## 📝 Approach
1.  Calculate `n` (length of the array).
2.  Compute `expected_sum` using the formula: $n \times (n + 1) // 2$.
3.  Compute `actual_sum` of the input array (using Python's `sum()` is efficient).
4.  Return `expected_sum - actual_sum`.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * We iterate through the array once to calculate the sum.
* **Space Complexity:** $O(1)$
    * We use only a few variables for storing sums.

> **Advanced Note (Bit Manipulation - XOR):**
> In languages with fixed integer sizes (like C++ or Java), the sum formula might cause **Integer Overflow** if $N$ is very large.
> In such cases, the **XOR** approach is safer : Use the parity (index and value has to come out twice)
> XORing all indices and all values will cancel out existing pairs, leaving only the missing number.