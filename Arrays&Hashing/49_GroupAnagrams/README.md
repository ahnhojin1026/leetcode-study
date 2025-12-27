# [LeetCode] 49. Group Anagrams

## 📌 Topic
* Hash Table
* String
* Sorting

## 💡 Idea / Intuition
An **Anagram** is a word formed by rearranging the letters of a different word.
Crucially, if two words are anagrams, **sorting their characters individually will result in the exact same string.**

We can use this sorted string as a **Key** in a Hash Map (Dictionary) to group the original words together.

## 📝 Approach
1.  **Initialize:** Create a dictionary (preferably `defaultdict(list)` for cleaner code).
2.  **Iterate:** Loop through each string in the input list.
3.  **Generate Key:** Sort the characters of the current string and join them to form a key (e.g., "cba" $\rightarrow$ "abc").
4.  **Group:** Append the original string to the list corresponding to the generated key in the dictionary.
5.  **Result:** Return the values of the dictionary as a list.

## ⏱️ Complexity
* **Time Complexity:** $O(N \cdot K \log K)$
    * $N$: Number of strings.
    * $K$: Maximum length of a string.
    * We iterate $N$ times, and for each string, we sort it which takes $O(K \log K)$.
* **Space Complexity:** $O(N \cdot K)$
    * We store all strings in the dictionary.