class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        i = 0
        while i < len(nums)-2 and nums[i] <= 0 :
            j = i+1
            k = len(nums)-1

            while j < k:
                s = nums[i]+nums[j]+nums[k]

                if s == 0:
                    output.append([nums[i],nums[j], nums[k]])
                    j+=1
                    k-=1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
                
                elif s < 0:
                    j+=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    
                
                else:
                    k-=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
            
            i+=1
            while i <len(nums)-2 and nums[i] <=0 and nums[i-1] == nums[i]:
                i+=1
        

        return output
            
                
            
                    
 

        