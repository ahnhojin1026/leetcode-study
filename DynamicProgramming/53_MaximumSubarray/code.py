class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # cur_max tracks the maximum sum of subarray ending at current position
        cur_max = 0
        # max_sum tracks the overall maximum sum found so far
        max_sum = nums[0]
        # Kadane's Algorithm
        for i,n in enumerate(nums):
            # cur_max is either extended by current number(cur_max + n) or starts new from current number(n)
            cur_max = max(cur_max + n,n)
            # max_sum is updated if cur_max is greater
            max_sum = max(max_sum,cur_max)

        return max_sum