# [LeetCode] {128}. {Longest Consecutive Sequence}

## Topic
* Arrays, Hashing

## 💡 Idea / Intuition
1. Use Set to remove repeating number (simplify the problem by removing it)
2. Check the number could be start of the sequence and calcuate only possible case.

* ## 📝 Approach
1. Put all the number in the `nums_set` Set. (prevent unnecessary calculation + constant lookup time)
2. Iterate through the Set
3. Check if the Set does not contain previous number, which means it could be starting of consecutive sequence
    * If Yes, Check how long the sequence is and track the longest one
    * If No, check the next number

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * Reason: Even in the worst case, each numebr in `nums_set` are visited twice (for loop, while loop) - (It looks like n^2 but it is not: `While` loop is execute only to the staring number and `for` loop is jumped by the if statement for non-starting number)

* **Space Complexity:** $O(N)$
    * Reason: Use Set to manage this problem (Maximum length is N)