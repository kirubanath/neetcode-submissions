class Solution:
    def trap(self, height: List[int]) -> int:
        
        # we should calculate how much does each bucket contribute

        left_max = [height[0]]
        for i in range(1,len(height)):
            left_max.append(max(height[i],left_max[i-1]))
        
        right_max = [height[-1]]
        for i in range(len(height)-2,-1,-1):
            right_max.append(max(height[i],right_max[len(height)-i-2]))
        right_max = right_max[::-1]

        output = 0
        for i in range(len(height)):
            output+= min(left_max[i],right_max[i])- height[i]
        
        return output


    
        
