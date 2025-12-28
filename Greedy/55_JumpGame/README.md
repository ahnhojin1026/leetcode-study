# [LeetCode] 55. Jump Game

## 📌 Topic
* Array
* Greedy

## 💡 Idea / Intuition
We need to determine if we can reach the last index starting from the first.
Instead of simulating every jump forward (which can be $O(N^2)$ or exponential), we can use a **Greedy approach backwards**.

## 📝 Approach
1.  Initialize `goal` to the last index.
2.  Iterate backwards from the second to last index down to 0.
3.  Check if the current index `i` can reach the `goal`:
    * Condition: `i + nums[i] >= goal`
4.  If yes, update `goal = i`.
5.  After the loop, check if `goal == 0`.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * We iterate through the array exactly once.
* **Space Complexity:** $O(1)$
    * We only use a single variable to store the target index.