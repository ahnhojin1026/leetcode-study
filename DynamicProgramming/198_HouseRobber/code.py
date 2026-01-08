class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base Cases
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2 :
            return max(nums[0], nums[1])
        # Opminization: Using rolling array to reduce space complexity
        dp = [0,0,0]

        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])
        
        for i in range(2,len(nums)):
            # Slide the window
            dp[0] = dp[1]
            dp[1] = dp[2]
            # Calculate the maximum amount that can be robbed up to the current house
            dp[2] = max(dp[0] + nums[i],dp[1])

        return dp[2]