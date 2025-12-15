class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(NlogN)  sort the array
        nums.sort()
        # list for storing answers
        ans = []

        # iterate through each number
        for i in range(len(nums)-2):
            # skip repeating case
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # remaining target sum
            target = -nums[i]
            # two pointer
            left = i + 1
            right = len(nums) - 1

            # move the two pointers toward the target
            while left < right:
                cur = nums[left] + nums[right]
                if cur == target:
                    ans.append([nums[i],nums[left],nums[right]])
                    left += 1
                    # move left pointer until new left value to skip duplicates
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                # adjust pointers based on comparison
                elif cur < target:
                    left += 1
                elif cur > target:
                    right -= 1
        
        return ans