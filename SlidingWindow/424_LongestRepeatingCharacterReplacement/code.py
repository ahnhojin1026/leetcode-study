class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window method
        left = 0
        max_len = 0
        # char_count to track the count of each character in the current window
        char_count = [0] * 26
        # max_count to track the count of the most frequent character in the viewed window
        max_count = 0

        for i in range(len(s)):
            char_count[ord(s[i]) - ord("A")] += 1
            # check only the updated value not the whole list (O(1))
            max_count = max(max_count,char_count[ord(s[i]) - ord("A")])
            # if the current window size minus the count of the most frequent character is greater than k, shrink the window from the left
            while (i - left + 1) > max_count + k:
                char_count[ord(s[left]) - ord("A")] -= 1
                left += 1

            
            max_len = max(max_len,(i - left + 1))

        return max_len