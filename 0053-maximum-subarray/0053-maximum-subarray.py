class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_sum = 0
        
        for n in nums:
            if (current_sum < 0):
                current_sum = 0
            current_sum += n
            current_max = max(current_sum, current_max)
            
        return current_max