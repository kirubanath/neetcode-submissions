# Fibonacci/optimized bottom up
class Solution:
    def climbStairs(self, n: int) -> int:

        if n < 2: # 0 is 1 and 1 is 1
            return 1

        one = 1
        two = 1


        for i in range(n-1):
            one,two = two, one + two
        
        return two



        
        