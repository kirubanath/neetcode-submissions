from math import ceil
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dist_speed = sorted(zip(position,speed))
        time = [(target-pos)/s for pos,s in dist_speed]
        

        stack = []
        for i in range(len(time)-1,-1,-1):
            if not stack:
                stack.append(time[i])
                continue
            
            if time[i] > stack[-1]:
                stack.append(time[i])
        
        return len(stack)
            

