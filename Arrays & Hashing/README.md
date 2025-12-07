# [LeetCode] {1}. {Two Sum}

## Topic
* Arrays, Hashing

## 💡 Idea / Intuition
1. Use two for loop will work(Brute Fore approach), but it needs O(n^2) time
2. Use of dictionary as hashmap to find the pair in O(1) for N inputs (uses of hash function)
* ## 📝 Approach
1. Initialize an empty dictionary (`hash_map`) to store values and their index number.
2. Iterate through the list using `enumerate`.
3. Cacluate the required pair and check if that exists
    * If Yes, return the pair List
    * If No, add the current numebr to `hash_map`

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * Reason: checking the dictionary takes constant time O(1), which is repeated for N inputs
* **Space Complexity:** $O(N)$
    * Reason: dictionary can take all n inputs