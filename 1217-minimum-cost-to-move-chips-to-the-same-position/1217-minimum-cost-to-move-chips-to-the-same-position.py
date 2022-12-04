class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count_odd = 0
        count_even = 0
        for i in range(len(position)):
            if position[i] % 2 == 1:
                count_odd += 1
            else:
                count_even += 1
        return min(count_odd, count_even)