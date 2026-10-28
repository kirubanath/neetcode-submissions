class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        from collections import defaultdict

        target_dict = {}

        for i in range(len(numbers)):
            n = target - numbers[i]
            if n in target_dict:
                return list((min(i+1,target_dict[n]+1),max(i+1,target_dict[n]+1)))
            
            target_dict[numbers[i]] = i
        


        