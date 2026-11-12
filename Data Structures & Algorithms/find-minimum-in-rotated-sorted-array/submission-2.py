class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l <=r:

            # if already sorted break:
            if nums[l] <= nums[r]:
                return nums[l]

            m = (l+r)//2

            # if m == l:
            #     return min(nums[l], nums[r])

            # if left half is sorted:
            if nums[l] <= nums[m]:

                # if right half is also sorted:
                if nums[m+1] <= nums[r]:
                    return nums[m+1]
                
                else:
                    l = m+1
            
            else:
                if nums[m-1] < nums[m]:
                    r = m -1
                else:
                    return nums[m]


            

        