"""
Brett's Algo : reduce number of slow pointer calculations

slow -> checkpoint
fast -> keeps moving
distance between each checkpoint keeps increasing exponentially
"""
class Solution:
    def process(self, n):
        output = 0

        while n: 
            d = n%10
            output += d**2
            n = n//10

        return output

    def isHappy(self, n: int) -> bool:

        slow = fast = n

        target_move = 1
        moved = 0

        while True:

            # Move fast forward till checkpoint
            if moved < target_move:
                
                # move
                fast = self.process(fast)

                # check and compare:
                if fast == 1:
                    return True
                
                if fast == slow:
                    return False
                
                moved +=1
            
            # Update the checkpoint
            else:
                
                # checkpoint
                slow = fast

                # move the checkpoint
                target_move = target_move*2    

                # reset count
                moved = 0

            






