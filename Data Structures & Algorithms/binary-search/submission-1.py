class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l = 0
        r = len(nums)-1

        while l<=r:
            t = (l+r)//2

            if nums[t] == target:
                return t
            elif nums[t] < target:
                l = t+1
            else:
                r = t-1
        
        return -1

