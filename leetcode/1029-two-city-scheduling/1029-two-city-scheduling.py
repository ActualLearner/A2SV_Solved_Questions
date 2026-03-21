class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key=lambda x: x[0] - x[1])
        
        sum_ = 0
        for i in range(n):
            if i < n // 2:
                sum_ += costs[i][0]
            else:
                sum_ += costs[i][1]
        
        return sum_