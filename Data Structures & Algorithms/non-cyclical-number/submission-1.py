class Solution:
    def digits(self,n):
        digits = [0,0,0,0]
        
        reminder = n
        for i in range(len(digits)):

            digits[i] = reminder // (10**(3-i))
            reminder = reminder % (10**(3-i))
        
        return digits


    def isHappy(self, n: int) -> bool:

        track = set()

        while True:

            # get the digits:
            d = self.digits(n)

            
            # get the sum of squares:
            s = 0
            for i in d:
                s+= i**2

            # check if its 1:
            if s == 1:
                return True
            
            # check if we are in a loop 
            if s in track:
                return False
            
            # if seen for first time add to the set
            track.add(s)
            
            # update the number itself to the new one:
            n = s

            
            
        