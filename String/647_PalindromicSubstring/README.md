# [LeetCode] 647. Palindromic Substrings

## 📌 Topic
* String Manipulation

## 💡 Idea / Intuition
This problem is a variation of `5_Longest Palindromic Substring`. Slight change of the `5_Longest Palindromic Substring` will give answer

## 📝 Approach
1.  Iterate through the string with index `i`.
2.  Treat `i` as the center for **odd-length** palindromes (`left=i, right=i`).
3.  Treat `i` and `i+1` as the center for **even-length** palindromes (`left=i, right=i+1`).
4. Use `expand` function to check the number of palindromic substring by checking the left and right character and expanding `s[left] == s[right]`
5. track the number of palindromes substring in variable `ans`

## ⏱️ Complexity
* **Time Complexity:** $O(N^2)$
    * We have $2N - 1$ centers, and each expansion takes $O(N)$ in the worst case.
* **Space Complexity:** $O(1)$
    * We used only limited variable for this problem