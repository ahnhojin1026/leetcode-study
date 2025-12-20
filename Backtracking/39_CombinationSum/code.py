class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        # use backtracking to find all combinations
        def backtracking(start_index: int, cur_sum: int, path: List[int]):
            # if the current sum equals target, add the path to ans
            if cur_sum == target:
                ans.append(path)
                return
            # if current suem exceeds target, return
            if cur_sum > target:
                return
            # allowing the same element to be chosen multiple times by starting from the current index
            for i in range(start_index,len(candidates)):
                backtracking(i,cur_sum+candidates[i],path + [candidates[i]])

        backtracking(0,0,[])

        return ans    