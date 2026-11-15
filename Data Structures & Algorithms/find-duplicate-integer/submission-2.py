# Method 3: Same idea as method 2 but instead of modifying the array itself
# If we think of the list itself as linked list..then there is a cycle!
# We can find the cycle using floyd's tortoise and hare algo
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow,fast = 0,0

        # We know for sure there is a cycle so while True is fine
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
        