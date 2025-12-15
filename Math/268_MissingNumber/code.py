class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_range = sum(nums)
        length = len(nums)
        # to Save space, use total sum to find the missing number
        return int(length * (length + 1)/2) - sum_range