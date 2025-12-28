class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals based on start time
        intervals.sort(key = lambda x : x[0])
        # print(intervals)
        ans = [intervals[0]]

        for i in range(1,len(intervals)):
            # if no overlap
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            # overlap update the end time
            else:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])

        # print(ans)
        return ans