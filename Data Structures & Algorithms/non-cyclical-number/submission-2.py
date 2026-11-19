class Solution:
    def process(self,n):

        output = 0

        while n:
            d = n%10
            output += (d**2)
            n = n//10
        
        return output

    def isHappy(self, n: int) -> bool:
        
        track = set()
        while True:
            n = self.process(n)
            if n == 1:
                return True
            
            if n in track:
                return False
            
            track.add(n)
        



        