class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):

            prev_interval = res[-1]
            interval = intervals[i]

            if prev_interval[1] < interval[0]:
                res.append(interval)
            
            else:
                res[-1] = [prev_interval[0], max(prev_interval[1],interval[1])]
        
        return res




