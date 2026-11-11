class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil

        # binary search between 1 and max
        ub = max(piles)
        lb = 1

        while lb <= ub:

            mid = (lb + ub)//2
            
            cur_hours = 0
            for p in piles:
                cur_hours += (p + mid - 1) // mid
            
            
            if cur_hours <= h:
                ub = mid -1
            
            else:
                lb = mid + 1
        
        return lb
            




        