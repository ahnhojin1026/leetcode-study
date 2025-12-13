class Solution:

    def expand(self, s: str, leftend: int, rightend: int) -> tuple[int, int]:
        max_length = 0
        max_start = leftend
        
        # first : check if the substring is expandable
        # second : check if the characters at both ends are equal
        while leftend >= 0 and rightend < len(s) and s[leftend] == s[rightend]:
            # if expanded, check if the new length is the maximum
            if rightend - leftend + 1 > max_length:
                max_length = rightend - leftend + 1
                max_start = leftend
            # update each ends
            leftend -= 1
            rightend += 1
        
        return max_length, max_start

    def longestPalindrome(self, s: str) -> str:
        max_substring_length = 1
        max_substring_start = 0
        
        for i in range(len(s)):
            # check the substring with odd number of characters (center : 'i'th character)
            length, start = self.expand(s, i, i)
            if length > max_substring_length:
                max_substring_length = length
                max_substring_start = start

            # check the substring with even number of characters (center : 'i'th,'i+1'th character)
            if i < len(s) - 1:
                length, start = self.expand(s, i, i + 1)
                if length > max_substring_length:
                    max_substring_length = length
                    max_substring_start = start

        return s[max_substring_start : max_substring_start + max_substring_length]
