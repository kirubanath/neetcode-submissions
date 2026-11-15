# Method 2: 
# Idea : The values are between 1-n meaning valid indices!
# That means if there is a duplicate then we will visit the same place twice!
# values are always positive as well!
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        i = 0
        while True:
            if nums[i] < 0:
                return i
            
            # Visit:
            temp = i
            i = nums[i]
            nums[temp] = -nums[temp]
        



        
            

        