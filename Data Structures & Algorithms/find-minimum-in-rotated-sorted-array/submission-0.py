class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1

        while l <=r:

            # if already sorted break:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r)//2

            # discard the sorted half and account for the element being discarded:
            if nums[l] <= nums[m]:
                # left half is sorted 
                l = m+1
                res = min(res, nums[m])
            else:
                # right half is sorted
                r = m -1
                res = min(res, nums[m])

        return res   
            
