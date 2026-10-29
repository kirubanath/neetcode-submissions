class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_area = 0

        while i < j:

            area = min(heights[i], heights[j])*(j-i)
            max_area = max(area, max_area)

            if heights[i] < heights[j]:
                i+=1
                while i <j and heights[i-1] ==heights[i]:
                    i+=1
                
            else:
                j-=1
                while i<j and heights[j+1] ==heights[j]:
                    j-=1
            
        return max_area
