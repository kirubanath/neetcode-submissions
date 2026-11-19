class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(x,n):

            if n == 0:
                return 1
            
            if x == 0:
                return 0
            
            res = (pow(x*x,n//2))

            if n%2:
                res = res*x
            
            return res
        
        res = pow(x,abs(n))
        return res if n > 0 else 1/res