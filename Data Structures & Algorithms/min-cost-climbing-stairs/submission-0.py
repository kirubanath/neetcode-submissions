class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        one = 0
        two = cost[-1]
        

        for i in range(len(cost)-2,-1,-1):
            one, two = two , cost[i] + min(one, two)
            
        return min(one,two)