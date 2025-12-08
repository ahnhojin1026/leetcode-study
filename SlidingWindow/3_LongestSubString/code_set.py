class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        max_substr_len = 0
        char_lookup_set = set()

        # Iterate with the right pointer
        for r in range(len(s)):
            # remove the duplicate until it is removed
            while s[r] in char_lookup_set:
                char_lookup_set.remove(s[l])
                l += 1
            # add the current char to window
            char_lookup_set.add(s[r])
            # update the maxlen every step
            max_substr_len = max(r - l + 1,max_substr_len)
        return max_substr_len


        