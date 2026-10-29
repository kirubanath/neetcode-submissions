class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        right_max = height[-1]
        
        l = 0
        r = len(height)-1
        water_level = 0


        while l < r : 
            
            if left_max < right_max:
                l+=1

                if left_max > height[l]:
                    water_level += left_max - height[l]
                else:
                    left_max = height[l]
                
            else:
                r-=1

                if right_max > height[r]:
                    water_level += right_max - height[r]
                else:
                    right_max = height[r]
            
        
        return water_level


