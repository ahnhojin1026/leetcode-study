class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # exception case (length 1)
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        # use Binary Search
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left+right)/2)
            # hit the target
            if nums[mid] == target:
                return mid
            # no cliff in cur range
            if nums[left] < nums[right]:
                # move left or right (just like normal binary search)
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
            # cliff in cur range
            else:
                # cliff in the left side
                if nums[mid] < nums[left]:
                    # move left or right (consider the cliff)
                    if nums[mid] < target and target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid -1
                # cliff in the right side
                else:
                    # move left or right (consider the cliff)
                    if nums[left] <= target and target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1

        return -1