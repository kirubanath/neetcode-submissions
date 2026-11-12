class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums)-1

        while l <=r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            
            # if left is sorted:
            if nums[l] <= nums[m]:

                # if target possible in left:
                if target >= nums[l] and target <= nums[m]:

                    # search in the left half
                    r = m-1
                
                else:

                    #search in the right half
                    l = m+1
            

            
            # if right is sorted:
            else:

                # if target possible in the right:
                if target <= nums[r] and target >= nums[m+1]:
                    l = m+1
                
                else:
                    r = m-1
        
        return -1
