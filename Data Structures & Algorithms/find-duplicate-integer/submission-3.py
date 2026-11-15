# Method 4: Bit Manipulation
# Check each set poisition 
# Since n < 10000 we just need to check 14 position
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        res = 0
        for i in range(14):

            mask = 1 << i

            # Check nums count
            nums_count = 0
            for num in nums:
                if num & mask:
                    nums_count +=1


            # Check normal count
            normal_count = 0
            for n in range(1,len(nums)):
                if n & mask:
                    normal_count +=1
            
            # If the bit is switched on for the duplicate number then count will be higher:
            if nums_count > normal_count:
                # switch on that bit in the result
                res = res | mask
        
        return res




