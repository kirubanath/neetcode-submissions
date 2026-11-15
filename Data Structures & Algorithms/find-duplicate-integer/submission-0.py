# Method 1:
# Simple hash
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                return n
            hashmap[n] = 1
        
        