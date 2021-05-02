class Solution:
    def intervalsSort(item):
        return item[0]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted(intervals,key=intervalsSort)
        i=0
        start=intervals[0][0]
        end=intervals[0][1]
        while i<len(intervals):
            if intervals[i][1]>=intervals[i+1][0]:
                start=intervals[i][0]
                end=intervals[i+1][1]
                
                
            
        