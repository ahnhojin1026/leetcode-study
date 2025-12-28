class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal of Jump Game is to reach the last index
        goal = len(nums) - 1
        
        # iterate from the second last index to the beginning
        for cur in range(len(nums)-2,-1,-1):
            # check if cur index can reach the goal
            if cur + nums[cur] >= goal:
                # if yes, update the goal to the current index
                goal = cur
        
        # if goal is updated to 0, it means we can reach the last index from the first index
        if goal == 0:
            return True
        else:
            return False