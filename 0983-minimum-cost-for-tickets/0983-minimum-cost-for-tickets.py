class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        best_way = {} #maps an index, with the least cost to get to the end
        
        def dfs(i):
            if (i == len(days)):
                return 0 #no cost if there are no days to travel on
            if (i in best_way.keys()):
                return best_way[i]
            
            best_way[i] = float("inf")
            
            for day, cost in zip([1,7,30], costs):
                j = i
                while (j < len(days) and days[j] < days[i] + day):
                    j += 1
                    best_way[i] = min(best_way[i], cost + dfs(j))
            return best_way[i]
            
         
        return dfs(0)