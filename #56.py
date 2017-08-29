# Author: Jin


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        res = []
        intervals.sort(key=lambda x: x.start)
        temp = intervals[0]
        for i in range(len(intervals) - 1):
            if temp.end < intervals[i + 1].start:
                res.append(temp)
                temp = intervals[i + 1]
            else:
                temp.end = max(intervals[i + 1].end, temp.end)
        res.append(temp)
        return res

s = Solution()
l = []
i1 = Interval(2, 3)
l.append(i1)
i2 = Interval(4, 5)
i3 = Interval(6, 7)
i4 = Interval(8, 9)
i5 = Interval(1, 10)
l.append(i2)
l.append(i3)
l.append(i4)
l.append(i5)
res = s.merge(l)
for x in res:
    print(x.start, x.end)