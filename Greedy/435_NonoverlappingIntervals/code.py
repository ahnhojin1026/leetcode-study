class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals based on end time, if end time is same then based on start time
        intervals.sort(key = lambda x : (x[1],x[0]))
        
        ans = 0
        cur_end = intervals[0][1]

        # greedy approach
        for i in range(1,len(intervals)):
            if intervals[i][0] >= cur_end:
                cur_end = intervals[i][1]
            else:
                ans += 1
        return ans
