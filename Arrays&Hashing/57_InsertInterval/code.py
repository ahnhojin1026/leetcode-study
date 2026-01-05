class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        if len(intervals) == 0:
            ans.append(newInterval)
            return ans


        for i in range(len(intervals)):
            # if the intervals are ahead of newInterval
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            # if the intervals are after newInterval
            elif intervals[i][0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]
            # merge overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        # if intervals has only merged intervals
        ans.append(newInterval)
        return ans

        