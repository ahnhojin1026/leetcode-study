class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # Dictionary to store the number of characters in t
        t_dict = {}
        s_dict = {}

        # count the characters in t
        for _, n in enumerate(t):
            if n in t_dict:
                t_dict[n] += 1
            else:
                t_dict[n] = 1
        # sliding window
        left = 0
        # number of characters that match the requirement exactly
        exact = 0

        # variable to store the minimum length and start position of the substring
        min_len = float('inf')
        start_pos = 0

        for right in range(len(s)):
            # count the characters in the current window
            if s[right] in s_dict:
                s_dict[s[right]] += 1
            else:
                s_dict[s[right]] = 1
            
            # check if the current character meets the requirement
            if s[right] in t_dict and t_dict[s[right]] == s_dict[s[right]]:
                exact += 1

            # try to shrink the window from the left
            while exact == len(t_dict):
                # update the minimum length and start position
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    start_pos = left
                # remove the leftmost character from the window
                remove_char = s[left]
                s_dict[remove_char] -= 1
                
                # check if the removed character causes the window to no longer meet the requirement
                if remove_char in t_dict and s_dict[remove_char] < t_dict[remove_char]:
                    exact -= 1
                # move the left pointer to the right
                left += 1 


        if min_len == float("inf"):
            return ""
        return s[start_pos : start_pos + min_len]