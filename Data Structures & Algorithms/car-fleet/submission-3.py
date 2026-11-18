class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position,speed), reverse = True)
        
        prev_time = 0
        fleet = 0


        for pos,s in pos_speed:

            time = (target - pos)/s
        
            if time > prev_time:
                fleet +=1
                prev_time = time
        
        return fleet
