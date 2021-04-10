"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda x: x.start)
        last = None
        for interval in intervals:
            if not last or last.end <= interval.start:
                last = interval
            else:
                return False
        return True
