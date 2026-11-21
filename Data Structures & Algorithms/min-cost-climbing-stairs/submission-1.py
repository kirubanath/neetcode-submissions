class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # cost at a step = cost of step + min (cost of step + 1 , cost of step +2)
        n = len(cost)
        total_cost= [0]* (n + 1)
        
        # for last step the cost is its own cost
        total_cost[n-1] = cost[n-1]

        for i in range(len(cost)-2,-1,-1):
            total_cost[i] = cost[i] + min(total_cost[i+1], total_cost[i+2])
        
        return min(total_cost[0], total_cost[1])
        