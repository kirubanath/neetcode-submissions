class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        # Init Heap
        heap = [elem*-1 for elem in nums[:k]]
        heapq.heapify(heap)

        # Init window hash map
        window = Counter(heap)

        # Init output array
        output = [-heap[0]]


        for incoming in range(k,len(nums)):
            outgoing = incoming-k

            # remove outgoing:
            window[-nums[outgoing]] -=1

            # add incoming:
            window[-nums[incoming]] +=1
            heapq.heappush(heap,-nums[incoming])

            # remove dead elements from the heap:
            while window[heap[0]] ==0:
                heapq.heappop(heap)
            
            # get the current max:
            output.append(-heap[0])
        
        return output

        

