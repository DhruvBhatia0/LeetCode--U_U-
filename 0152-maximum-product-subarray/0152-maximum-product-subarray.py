class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        max_r = 1
        min_r = 1
        
        for n in nums:
            temp_max = max(max_r * n, min_r * n)
            temp_min = min(min_r * n, max_r * n)
            result = max( result, max(n, max(temp_max, temp_min)))
            max_r = max(temp_max, n)
            min_r = min(temp_min, n)
            
        return result
            