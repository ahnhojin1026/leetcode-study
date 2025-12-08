class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_substr_len = 0
        # initial dictionary
        # key : character, value : index of the coresponding character
        char_lookup_dict = {} 

        # Iterate with the right pointer
        for r in range(len(s)):
            # if character exists in valid window context, update the window size immediately
            if s[r] in char_lookup_dict and char_lookup_dict[s[r]] >= l:
                # update left pointer (not lineary but using the value in the dictionary, update is done in constant time)
                l = char_lookup_dict[s[r]] + 1
                
            # add the current char to window
            char_lookup_dict[s[r]] = r
            # update the maxlen every step
            max_substr_len = max(r - l + 1,max_substr_len)
        return max_substr_len


        