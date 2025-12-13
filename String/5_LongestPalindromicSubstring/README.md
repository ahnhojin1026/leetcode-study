# [LeetCode] 5. Longest Palindromic Substring

## 📌 Topic
* String Manipulation

## 💡 Idea / Intuition
1. **Symmetry:** A palindrome mirrors around its center. So at first I tried with DP method
2. **Center Expansion:** Instead of checking all substrings we can **expand outwards** from every possible center.
3. There are $2N - 1$ centers: $N$ single-character centers (odd length) and $N-1$ centers between characters (even length).

## 📝 Approach
1. Iterate through the string, treating each index `i` as the center.
2. **Expand** in two ways for each `i`:
    * **Odd Length:** Center is `s[i]`. Initialize `left=i`, `right=i`.
    * **Even Length:** Center is between `s[i]` and `s[i+1]`. Initialize `left=i`, `right=i+1`.
3. In the helper function, expand while `left >= 0`, `right < len(s)`, and `s[left] == s[right]`.
4. Update the global maximum start and end indices whenever a longer palindrome is found.

## ⏱️ Complexity
* **Time Complexity:** $O(N^2)$
    * We have $O(N)$ centers, and expanding takes $O(N)$ in the worst case.
* **Space Complexity:** $O(1)$
    * We only use a few variables