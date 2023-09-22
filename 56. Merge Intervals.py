class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        idx = 0
        intervals = sorted(intervals, key=lambda x: (x[0]))
        print(intervals)
        while idx < len(intervals) - 1:
            if intervals[idx][1] >= intervals[idx + 1][0]:
                intervals[idx][1] = max(intervals[idx + 1][1], intervals[idx][1])
                intervals.pop(idx + 1)
            else:
                idx += 1

        return intervals

