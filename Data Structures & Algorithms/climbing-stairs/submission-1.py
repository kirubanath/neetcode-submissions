# Recursion with cache
# Just add cache lookup for solution 1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        cache = [-1]*(n+1)
        cache[-1] = 1

        
        def steps(i,n):

            if i > n:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = steps(i+1,n) + steps(i+2,n)
            
            return cache[i]
        
        return steps(0,n)
            

            

        