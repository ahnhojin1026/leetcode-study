class Solution:
    # binary search to find the index to replace
    # goal : find the first element >= target
    def bin_search(self, left: int, right: int, arr: List[int], target: int) -> int:
        ''' return the index of the first element >= target '''
        mid = 0
        while left < right:
            mid = int((left + right) / 2)
            if arr[mid] == target:
                # if same num exist, replace it
                return mid
            elif arr[mid] < target:
                left = mid + 1
            # if arr[mid] > target: mid might be the answer so we do not do mid - 1
            elif arr[mid] > target:
                right = mid
        return right
            
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        # list to store the increasing subsequence
        ans = [nums[0]]

        for i in range(1,len(nums)):

            # if current num is greater than the last num in ans, append it
            if nums[i] > ans[len(ans)-1]:
                ans.append(nums[i])
            # else, find the index to replace
            elif nums[i] != ans[len(ans)-1]:
                change_index = self.bin_search(0, len(ans)-1, ans, nums[i])
                ans[change_index] = nums[i]
            # print(ans)
        # return the length of ans (note : ans is not the actual subsequence)
        return len(ans)