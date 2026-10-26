class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for elem in nums:
            if elem in nums_dict:
                return True
            nums_dict[elem]=0
        return False


        