class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get the frequency of all the num
        fd = defaultdict(int)
        for num in nums:
            fd[num]+=1
        
        # transfer the frequency to buckets:
        buckets = [[] for _ in range(len(nums)+1)] # freq 0 to len(nums)

        for num in fd:
            buckets[fd[num]].append(num)
        
        # get the top k 
        res = []
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            

