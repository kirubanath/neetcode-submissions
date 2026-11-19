class Solution:
    def myPow(self, x: float, n: int) -> float:

        if not n:
            return 1
        
        if n == -1:
            return 1/x
        
        res = (self.myPow(x,n//2))**2

        if n%2:
            res = res * x    
    
        
        return res 

        