class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # initial dictionary
        # Value : Index number to store visited number

        for i, n in enumerate(nums):
            if (target - n) in hash_map: # if proper pair exists, return the pair in List
                return [hash_map[target-n], i]
            hash_map[n] = i # if pair does not exist, add the number with index to hash_map
        return