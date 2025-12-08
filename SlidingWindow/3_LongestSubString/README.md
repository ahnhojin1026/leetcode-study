# [LeetCode] {3}. {Longest Substring Without Repeating characters}

## Topic
* Sliding Window

## 💡 Idea / Intuition
1. Use two for loop will work(Brute Fore approach), but it needs O(n^2) time
2. We can use a Two Pointer technique (Sliding Window) combined with a Set to check for duplicates efficiently.
3. (new) optimize the two pointer technique with Dictionary in order to replace slowly shrinking window to instant shrink

## 📝 Approach 
1. Initialize left pointer to 0 and an empty set char_lookup_set.
2. Iterate through the string using the right pointer (for r in range(len(s))).
3. if s[right] is already in char_lookup_set, remove s[left] and increment left pointer until no more repeating occure in char_lookup_set (update : move to char_index_map[char] + 1, the first place without repeating character)
4. Add the current character s[right] to the set. (update : add the character and its index to dictionary)
5. Update the max_substr_len (r - l + 1) at each step.

## ⏱️ Complexity
* **Time Complexity:** $O(N)$
    * Reason: each character is added to the set at most once and removed at most once.
* **Space Complexity:** $O(min(N,M))$ (M is the number of different character)
    * Reason: dictionary can take all n inputs of M kind of charset