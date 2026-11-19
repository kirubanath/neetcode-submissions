# Fast and Slow pointers for any cycles!
class Solution:
    def process(self,n):
        output = 0

        while n:
            d = n%10
            output += d**2
            n = n//10
        
        return output

    def isHappy(self, n: int) -> bool:

        slow = fast = n
        while True:

            slow = self.process(slow)
            fast = self.process(self.process(fast))

            if slow == 1 or fast == 1:
                return True
            
            if slow == fast:
                return False
        