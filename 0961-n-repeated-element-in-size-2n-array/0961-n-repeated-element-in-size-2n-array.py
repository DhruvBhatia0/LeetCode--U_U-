class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return max(set(nums), key = nums.count)