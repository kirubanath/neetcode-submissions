class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        f_dict = defaultdict(int)

        for n in nums:
            f_dict[n]+=1
        
        buckets = [[] for _ in range(len(nums)+1)]
        for n in f_dict:
            buckets[f_dict[n]].append(n)
        
        count = k
        output_list = []
        for i in range(len(buckets)-1,-1,-1):
            for elem in buckets[i]:
                output_list.append(elem)
                count-=1
                if not count:
                    return output_list

        


        