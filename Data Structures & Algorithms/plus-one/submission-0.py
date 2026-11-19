class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        reminder = 1

        for i in range(len(digits)-1,-1,-1):

            d = digits[i] + reminder
            res.append(d%10)
            reminder = d//10
        
        if reminder:
            res.append(reminder)

        return res[::-1]




