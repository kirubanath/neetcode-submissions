class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        f_dict = defaultdict(int)

        
        for n in nums:
            f_dict[n]+=1
            
        
        f_list = sorted(f_dict.items(), key = lambda x:x[1], reverse = True)

        return [x[0] for x in f_list[:k]]
        


        