class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = customers[0][0]
        total_wt = 0
        for c in customers:
            time = max(time,c[0])
            time += c[1]
            total_wt += (time-c[0])
        return total_wt/len(customers)