class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use Two Pointer Approach
        left = 0
        right = len(height) - 1
        # Initialize max amount of water
        max_amount_water = 0


        while left < right:
            # update the max amount of water
            max_amount_water = max(max_amount_water, min(height[left],height[right])*(right-left))
            
            # Our method is to move from the most wide case to the less wide case
            # shrinking the one with larger height will only lead to less amount of water
            # lets shrinkt the one with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

                
        return max_amount_water
        