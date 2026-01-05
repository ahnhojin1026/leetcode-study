# [LeetCode] 62. Unique Paths

## 📌 Topic
* Math (Combinatorics)
* Dynamic Programming

## 💡 Idea / Intuition
We need to move from the top-left $(0,0)$ to the bottom-right $(m-1, n-1)$.
The robot can only move **Down** or **Right**.

To reach the destination, regardless of the path taken, the robot **must** make exactly:
* $m - 1$ moves Down
* $n - 1$ moves Right

Total steps = $(m - 1) + (n - 1) = m + n - 2$.
The problem effectively becomes: "In a sequence of $m+n-2$ moves, choose which $n-1$ moves are 'Right'".
This is a classic combination problem: $_{m+n-2}\mathrm{C}_{n-1}$.

## 📝 Approach
1.  **Formula:** Calculate $\binom{m+n-2}{n-1} = \frac{(m+n-2)!}{(m-1)!(n-1)!}$.
2.  **Optimization:** To minimize the number of multiplications/divisions, ensure we choose the smaller value for the denominator (since $\binom{N}{K} = \binom{N}{N-K}$).
3.  **Calculation:** Iteratively multiply the numerator and divide by the denominator.

## ⏱️ Complexity
* **Time Complexity:** $O(\min(M, N))$
    * We iterate proportional to the smaller dimension to calculate the factorial.
    * (Note: Standard DP approach would be $O(M \times N)$).
* **Space Complexity:** $O(1)$
    * Only a few variables are used for calculation.