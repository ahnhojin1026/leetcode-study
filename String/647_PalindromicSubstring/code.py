class Solution:
    def countSubstrings(self, s: str) -> int:
        # numbers of palindromic substring
        ans = 0 
        
        # O(N^2) approach

        def expand (s: str, center_left: int, center_right: int) -> int:
            '''
            function for center substring expansion
            
            s : input string
            :type s: str
            :param center_left: the center of expansion (left)
            :type center_left: int
            :param center_right: the center of expansion (right)
            :type center_right: int
            :return: number of palindromic substrings from the center
            :rtype: int
            '''
            substring_num = 0
            left = center_left
            right = center_right

            # loop until the substring is expandable (in range, palindromic)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                substring_num += 1
                left -= 1
                right += 1
            return substring_num

        for i, _ in enumerate(s):
            # check for odd-length palindromes
            ans += expand(s,i,i)
            
            # check for even-length palindromes
            if i != (len(s)-1) and s[i] == s[i+1]:
                ans += expand(s,i,i+1)
            
        return ans
        