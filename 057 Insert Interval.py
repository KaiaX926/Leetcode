class Solution(object):
    def insert(self,intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort()
        
        if len(intervals) <= 1:
            return intervals
        res = []
        i = 1
        
        while i < len(intervals):
            #print(intervals)
            if intervals[i][0] <= intervals[i-1][1]:
                x1 = min(intervals[i][0],intervals[i-1][0])
                x2 = max(intervals[i][1],intervals[i-1][1])
                x = [[x1,x2]]
                intervals = intervals[:i-1] + x + intervals[i+1:]
                
            else:
                i += 1
        return intervals
