class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove the repeating number using Set
        nums_set = set(nums)
        
        longest_length = 0
        for start in nums_set:
            # check if start could be start of sequence by checking start-1 exists
            if start-1 not in nums_set:
                cur_length = 1
                cur_num = start
                # keep check consecutive number
                while cur_num+1 in nums_set:
                    cur_length += 1
                    cur_num += 1
                
                longest_length = max(longest_length, cur_length)

        return longest_length