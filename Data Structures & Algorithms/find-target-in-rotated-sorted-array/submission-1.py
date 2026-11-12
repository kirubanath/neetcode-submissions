"""
1. Break
2. Check the sorted part for target possibility and discard the app. part
3. recheck the remaining part
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l,r):

            while l <=r:
                m = (l+r)//2

                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l+=1
                else:
                    r-=1
            return -1


        l,r = 0, len(nums)-1

        while l<=r:
            

            # if its already sorted then simple binary search:
            if nums[l] <= nums[r]:
                
                return binary_search(l,r)
            
            m = (l+r)//2
            
            if nums[m] == target:
                return m


            # check if the left is sorted:
            if nums[l] <= nums[m]:
                

                # check if target possible:
                if (nums[l] <= target) and (target <= nums[m]):
                    return binary_search(l,m)
                
                # if not just discard and move:
                else:
                    l = m+1
            
            else:

                #check if target is possibe on the right:
                if (nums[m+1] <= target) and (target<= nums[r]):
                    print(m+1,r)
                    return binary_search(m+1,r)
                
                # if not discard the right and move:
                else:
                    r = m-1
            


