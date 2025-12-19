class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        # rotated n times -> given array is sorted
        if nums[left] < nums[right]:
            return nums[left]
            
        # key : find the decending part (maximum -> minium) in Binary Search
        while left < right-1:
            mid = int((left + right) / 2)
            # if mid is the point of cliff, return immidiately
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            # if cliff is in the left part
            if nums[mid] < nums[left]:
                right = mid
            # if cliff is in the right part
            else:
                left = mid
        return nums[right]
        