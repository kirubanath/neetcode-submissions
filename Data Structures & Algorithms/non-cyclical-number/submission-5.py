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
        target = 1
        move = 0

        while True:

            fast = self.process(fast)
            move = move + 1

            if fast == 1:
                return True
            
            if fast == slow:
                return False
            
            if move == target:
                slow = fast
                move = 0
                target = target * 2
        