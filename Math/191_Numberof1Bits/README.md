# [LeetCode] 191. Number of 1 Bits

## 📌 Topic
* Bit Manipulation
* Divide and Conquer

## 💡 Idea / Intuition
The problem asks for the Hamming Weight (population count) of a 32-bit integer.
Instead of iterating through all 32 bits one by one ($O(K)$), we can use a **Divide and Conquer** strategy to count bits in parallel.

This method acts like a **parallel adder tree**:
1.  Count 1s in every adjacent **2-bit** pair.
2.  Sum those counts into adjacent **4-bit** groups.
3.  Sum those into **8-bit** groups, and so on, until we reach 32 bits.

This allows us to perform the count in $O(\log N)$ steps (specifically 5 steps for 32 bits) without any loops or branches.

## 📝 Approach
We use specific bitmasks to isolate and sum chunks of bits:
1.  `mask1 (0x55...)`: `0101...` $\rightarrow$ Adds adjacent bits to form 2-bit counts.
2.  `mask2 (0x33...)`: `0011...` $\rightarrow$ Adds adjacent 2-bit groups to form 4-bit counts.
3.  `mask3 (0x0f...)`: `00001111...` $\rightarrow$ Adds adjacent 4-bit groups.
4.  `mask4 (0x00ff...)`: Adds adjacent 8-bit groups.
5.  `mask5 (0xffff...)`: Adds adjacent 16-bit groups.

## ⏱️ Complexity
* **Time Complexity:** $O(1)$
    * It always takes exactly 5 operations for a 32-bit integer, regardless of the number of 1s.
* **Space Complexity:** $O(1)$
    * No extra space used.