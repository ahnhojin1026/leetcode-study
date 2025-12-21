# [LeetCode] 300. Longest Increasing Subsequence

## 📌 Topic
* Binary Search

## 💡 Idea / Intuition
The problem asks for the length of the longest strictly increasing subsequence.
While a standard DP approach takes $O(N^2)$, we can optimize this to $O(N \log N)$ by maintaining a **"Tails" array**.

The `tails` array stores the **smallest ending element** of all increasing subsequences of length `i+1`.
By keeping the ending elements as small as possible, we maximize the potential to extend the subsequence later.

## 📝 Approach
1.  **Initialize:** Create a `tails` list with the first element of `nums`.
2.  **Iterate:** Loop through the rest of `nums`:
    * **Case 1 (Extend):** If the current number is **larger** than the last element of `tails`, append it. This means we found a longer increasing subsequence.
    * **Case 2 (Update):** If the current number is **smaller or equal**, find the **first element in `tails` that is >= current number** using **Binary Search** and replace it.
        * This updates the potential for a subsequence of that specific length to end with a smaller number, which is always better for future additions.
3.  **Result:** The length of the `tails` list is the length of the LIS.

## 📕 Mathematical Proof
To prove that this greedy approach yields the correct LIS length, we use **Mathematical Induction**.

### 1. Definition & Invariant
Let `tails[k]` be the **smallest ending element** of an increasing subsequence of length `k+1`.
* **Invariant:** The `tails` array is always strictly increasing ($tails[0] < tails[1] < \dots$).
    * *Proof:* A subsequence of length $L+1$ is formed by appending an element to a subsequence of length $L$. Thus, the ending element of length $L+1$ must be strictly larger than the ending element of length $L$.

### 2. Inductive Step
Assume that for the first $N$ elements, `tails` correctly stores the smallest tail for each length. Now consider the $(N+1)$-th element, let's call it $X$.

* **Case 1: $X >$ all elements in `tails`**
    * We can extend the longest existing subsequence (length $L$) by appending $X$.
    * This creates a valid increasing subsequence of length $L+1$ ending with $X$. The algorithm correctly appends $X$, increasing the LIS length.

* **Case 2: $X$ falls in the middle ($tails[i-1] < X \le tails[i]$)**
    * We find the index $i$ such that $tails[i]$ is the first element $\ge X$.
    * We update $tails[i] = X$.
    * **Validity:** Since $tails[i-1] < X$, we can attach $X$ after the subsequence of length $i$ (ending at $tails[i-1]$) to form a valid increasing subsequence of length $i+1$.
    * **Optimality:** Since $X \le tails[i]$, updating `tails[i]` with $X$ maintains the definition of "smallest ending element." A smaller tail is always advantageous for future extensions.

### 3. Conclusion
By induction, after processing all elements, the length of the `tails` array represents the maximum possible length of an increasing subsequence found so far.



## ⏱️ Complexity
* **Time Complexity:** $O(N \log N)$
    * We iterate through `nums` ($N$), and for each element, we might perform a Binary Search ($O(\log N)$).
* **Space Complexity:** $O(N)$
    * The `tails` list can grow up to size $N$ in the worst case (strictly increasing input).