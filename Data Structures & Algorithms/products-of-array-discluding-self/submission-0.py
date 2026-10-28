class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_without_zero = 1
        zero_index = None
        num_zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index = i
                num_zeros +=1
                if num_zeros >1:
                    return [0]*len(nums)
            
            else:
                product_without_zero *= nums[i]
        
        if num_zeros ==1:
            output = [0 for _ in range(len(nums))]
            output[zero_index] = product_without_zero
        
        else:
            output = [0 for _ in range(len(nums))]
            for i in range(len(nums)):
                output[i] = int(product_without_zero/nums[i])
        
        return output
        

            



