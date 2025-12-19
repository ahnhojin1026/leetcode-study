class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # exception for length `1`
        if len(nums) == 1:
            return nums[0]
        # cur_max, cur_min : the maximum/minimum product ending with nums[i]
        cur_max = nums[0]
        cur_min = nums[0]

        # the global maximum product subarray
        ans = nums[0]

        for i in range(1,len(nums)):
            # if nums[i] is non-negative : cur_max and cur_min are updated normally
            if nums[i] >= 0:
                cur_max = max(cur_max*nums[i], nums[i])
                cur_min = min(cur_min*nums[i], nums[i])
            # if nums[i] is negative : cur_max and cur_min are updated by swapping their roles
            else:
                new_cur_max = max(cur_min*nums[i], nums[i])
                cur_min = min(cur_max*nums[i], nums[i])
                cur_max = new_cur_max
            # update the global maximum product subarray
            ans = max(ans,cur_max)
        return ans