"""
Monotonic stack:
Each height extends till it sees something smaller and pops
Each new small height takes over from the previous popped
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            

            rect_height = heights[i]
            rect_start  = i

            while stack and stack[-1][0] >= rect_height:

                # Pop the taller height from the stack
                popped_height, popped_start = stack.pop()

                # Update max area
                popped_area = popped_height * (i - popped_start)
                max_area = max(max_area, popped_area)

                # Update the rect_start
                rect_start = popped_start
            
            stack.append((rect_height,rect_start))
        
        # Now once out of the loop, check for everything remaining in the stack
        while stack:
            popped_height, popped_start = stack.pop()

            # Update max area
            popped_area = popped_height * (len(heights) - popped_start)
            max_area = max(max_area, popped_area)
        
        return max_area

        
        